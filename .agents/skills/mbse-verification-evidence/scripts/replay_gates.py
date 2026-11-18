"""Replay inclusive numeric gates in an issued Markdown table against source-derived cases."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError(f"Use an integer, decimal or fraction, got {value!r}")
    return Fraction(value)


def cells(line):
    return [cell.strip() for cell in line.strip()[1:-1].split("|")]


def issued_rows(text, key, columns):
    """Select exactly one plain pipe table by its header, outside fenced code."""
    lines = text.splitlines()
    headers = []
    fence = ""
    for i, line in enumerate(lines[:-1]):
        stripped = line.strip()
        marker = re.match(r"^(`{3,}|~{3,})", stripped)
        if marker:
            if not fence:
                fence = marker[1]
            elif stripped.startswith(fence) and not stripped.strip(fence[0]):
                fence = ""
            continue
        if fence or not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        names = cells(line)
        rule = lines[i + 1].strip()
        if (key in names and set(columns) <= set(names)
                and rule.startswith("|") and rule.endswith("|")
                and len(cells(rule)) == len(names)
                and all(re.fullmatch(r":?-{3,}:?", c) for c in cells(rule))):
            if len(names) != len(set(names)):
                raise ValueError("Duplicate column in selected table")
            headers.append((i, names))
    if len(headers) != 1:
        raise ValueError(f"Expected one matching table, found {len(headers)}")
    i, names = headers[0]
    rows = {}
    for index in range(i + 2, len(lines)):
        raw = lines[index].strip()
        if not raw.startswith("|"):
            break
        parts = cells(raw)
        if not raw.endswith("|") or len(parts) != len(names):
            raise ValueError(f"Malformed table row at line {index + 1}")
        row = dict(zip(names, parts))
        label = row[key]
        if not label or label in rows:
            raise ValueError(f"Missing or duplicate event at line {index + 1}")
        rows[label] = (index + 1, row)
    return rows


def keys(obj, required, optional=()):
    if not isinstance(obj, dict) or not set(required) <= obj.keys() <= set(required) | set(optional):
        raise ValueError(f"Expected fields {required} with optional {optional}, got {obj!r}")


def replay(text, spec):
    keys(spec, ("event_column", "gates", "cases"))
    gates = spec["gates"]
    if not isinstance(gates, dict) or not gates or spec["event_column"] in gates:
        raise ValueError("Provide at least one distinct numeric gate column")
    for column in gates.values():
        keys(column, ("sense", "unit"))
        if column["sense"] not in ("min", "max") or not isinstance(column["unit"], str):
            raise ValueError("Each gate needs min or max and a unit string")
    rows = issued_rows(text, spec["event_column"], gates)
    if not isinstance(spec["cases"], list) or not spec["cases"]:
        raise ValueError("No replay cases")
    checks = []
    for case in spec["cases"]:
        keys(case, ("name", "basis", "initial", "steps"))
        if not all(isinstance(case[k], str) and case[k].strip() for k in ("name", "basis")):
            raise ValueError("Identify the case and source basis")
        keys(case["initial"], gates)
        state = {col: number(v) for col, v in case["initial"].items()}
        if not isinstance(case["steps"], list) or not case["steps"]:
            raise ValueError("A case requires at least one step")
        for index, step in enumerate(case["steps"]):
            keys(step, ("event", "expect"), ("delta",))
            if step["expect"] not in ("allow", "block"):
                raise ValueError("Expected action must be allow or block")
            if step["expect"] == "block" and index != len(case["steps"]) - 1:
                raise ValueError("An expected block ends the branch")
            delta = step.get("delta", {})
            keys(delta, (), gates)
            for col, change in delta.items():
                state[col] += number(change)
            line, row = rows[step["event"]]
            violations = []
            for col, gate in gates.items():
                match = re.fullmatch(r"([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*" +
                                     re.escape(gate["unit"]), row[col])
                if not match:
                    raise ValueError(f"Expected a numeric gate in {col!r} at line {line}, got {row[col]!r}")
                limit = number(match[1])
                violates = state[col] < limit if gate["sense"] == "min" else state[col] > limit
                if violates:
                    violations.append({"column": col, "sense": gate["sense"], "issued": row[col]})
            actual = "block" if violations else "allow"
            checks.append({"case": case["name"], "line": line, "event": step["event"],
                           "state": {col: str(v) for col, v in state.items()},
                           "expected": step["expect"], "actual": actual, "violations": violations})
            if actual != step["expect"]:
                break  # Later states on this planned branch are unreachable.
    return checks


def unique_fields(pairs):
    data = {}
    for k, v in pairs:
        if k in data:
            raise ValueError(f"Duplicate JSON field {k!r}")
        data[k] = v
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", type=Path)
    parser.add_argument("cases", type=Path)
    args = parser.parse_args()
    try:
        raw = args.table.read_bytes()
        cases = args.cases.read_bytes()
        spec = json.loads(cases, parse_float=str, object_pairs_hook=unique_fields)
        checks = replay(raw.decode("utf-8"), spec)
    except (KeyError, TypeError, ValueError, OSError, ZeroDivisionError) as error:
        parser.exit(2, f"Invalid replay input: {error}\n")
    passed = all(c["expected"] == c["actual"] for c in checks)
    print(json.dumps({"table_sha256": hashlib.sha256(raw).hexdigest(),
                      "cases_sha256": hashlib.sha256(cases).hexdigest(),
                      "passed": passed, "checks": checks}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

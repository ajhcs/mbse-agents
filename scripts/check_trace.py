"""Check selected trace/evidence invariants; does not judge semantic adequacy."""
from pathlib import Path
import argparse
import hashlib
import json
import re


def local_file(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError(f"Artifact escapes baseline directory: {relative}")
    return path


def _check(data, base):
    errors = []
    groups = ["sources", "requirements", "functions", "components", "interfaces", "verification", "evidence"]
    maps = {}
    ids = set()
    for group in groups:
        rows = data.get(group)
        if not isinstance(rows, list) or not rows:
            errors.append(f"Missing/nonempty list required: {group}")
            maps[group] = {}
            continue
        maps[group] = {}
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
                errors.append(f"Invalid ID record in {group}")
                continue
            if row["id"] in ids:
                errors.append(f"Duplicate ID: {row['id']}")
            ids.add(row["id"])
            maps[group][row["id"]] = row

    def link(owner, value, group):
        if not isinstance(value, str) or value not in maps[group]:
            errors.append(f"{owner}: unresolved {group} link {value}")

    def links(owner, values, group):
        if not isinstance(values, list) or not values:
            errors.append(f"{owner}: missing {group} links")
        else:
            for value in values:
                link(owner, value, group)

    if data.get("schema_version") != 1 or not data.get("scope"):
        errors.append("Require schema_version=1 and explicit scope")
    for row in maps["sources"].values():
        try:
            if not local_file(base, row["artifact"]).is_file():
                errors.append(f"{row['id']}: missing source artifact")
        except (KeyError, TypeError, ValueError):
            errors.append(f"{row['id']}: invalid source artifact")
    for row in maps["requirements"].values():
        link(row["id"], row.get("source"), "sources")
        links(row["id"], row.get("functions"), "functions")
        if row.get("status") != "proposed":
            errors.append(f"{row['id']}: this teaching schema requires proposed requirement status")
    for row in maps["functions"].values():
        links(row["id"], row.get("components"), "components")
    for row in maps["interfaces"].values():
        for end in ["from", "to"]:
            link(row["id"], row.get(end), "components")
    covered = set()
    for row in maps["verification"].values():
        links(row["id"], row.get("requirements"), "requirements")
        covered.update(row.get("requirements", []) if isinstance(row.get("requirements"), list) else [])
        link(row["id"], row.get("evidence"), "evidence")
    for requirement in maps["requirements"]:
        if requirement not in covered:
            errors.append(f"{requirement}: no planned verification")
    outcomes = {}
    for row in maps["evidence"].values():
        if row.get("status") not in {"planned", "executed"}:
            errors.append(f"{row['id']}: unsupported evidence status")
        if row.get("status") != "executed":
            continue
        try:
            record = json.loads(local_file(base, row["artifact"]).read_text(encoding="utf-8"))
            if row.get("scope") != data["scope"] or record.get("scope") != row["scope"]:
                errors.append(f"{row['id']}: evidence scope mismatch")
            config = record.get("configuration")
            if not isinstance(data.get("configuration_files"), list) or not data["configuration_files"] or not isinstance(config, dict) or set(config) != set(data["configuration_files"]):
                errors.append(f"{row['id']}: incomplete configuration coverage")
            if not isinstance(config, dict) or not config:
                errors.append(f"{row['id']}: missing configuration hashes")
            else:
                for relative, digest in config.items():
                    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) or hashlib.sha256(local_file(base, relative).read_bytes()).hexdigest() != digest:
                        errors.append(f"{row['id']}: stale or invalid configuration {relative}")
            results = record.get("results")
            if not isinstance(results, list) or not results:
                errors.append(f"{row['id']}: missing executed outcomes")
            else:
                for result in results:
                    ident = result["verification"]
                    link(row["id"], ident, "verification")
                    if ident in outcomes:
                        errors.append(f"Duplicate executed outcome: {ident}")
                    if result.get("result") not in {"pass", "fail", "inconclusive"}:
                        errors.append(f"{ident}: invalid result")
                    if not result.get("observed"):
                        errors.append(f"{ident}: missing observations")
                    if ident in maps["verification"] and maps["verification"][ident].get("evidence") != row["id"]:
                        errors.append(f"{ident}: outcome stored in the wrong evidence artifact")
                    outcomes[ident] = result.get("result")
        except (OSError, ValueError, TypeError, KeyError):
            errors.append(f"{row['id']}: missing or malformed executed artifact/configuration")
    for row in maps["verification"].values():
        evd = maps["evidence"].get(row.get("evidence"), {})
        if evd.get("status") == "executed" and row["id"] not in outcomes:
            errors.append(f"{row['id']}: executed evidence has no outcome")
    # Conservative: every linked procedure must pass before calling a requirement covered by passing evidence.
    passing = []
    for requirement in maps["requirements"]:
        activities = [r["id"] for r in maps["verification"].values() if requirement in r.get("requirements", [])]
        if activities and all(outcomes.get(i) == "pass" for i in activities):
            passing.append(requirement)
    return errors, {"requirements": len(maps["requirements"]), "requirements_with_passing_model_evidence": len(passing),
                    "executed_procedures": len(outcomes), "scope": data.get("scope"), "acceptance": "not_assessed"}


def check(data, base):
    try:
        return _check(data, Path(base))
    except (KeyError, TypeError, ValueError, AttributeError) as error:
        return [f"Malformed baseline: {error}"], {"acceptance": "not_assessed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    args = parser.parse_args()
    try:
        errors, summary = check(json.loads(args.baseline.read_text(encoding="utf-8")), args.baseline.parent)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, str(error) + "\n")
    print(json.dumps(summary, indent=2))
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")


if __name__ == "__main__":
    main()

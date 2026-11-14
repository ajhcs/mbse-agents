"""Check reference-baseline links and evidence integrity, not physical validity."""
from datetime import datetime
from pathlib import Path
import argparse
import hashlib
import json
import math
import re
import sys

_LOADED_MODULE_CODE = sys._getframe().f_code


def local_file(base, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError(f"Require a nonempty relative artifact path: {relative!r}")
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError(f"Artifact escapes baseline directory: {relative}")
    return path


def _finite_json(value):
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(isinstance(k, str) and _finite_json(v) for k, v in value.items())
    if isinstance(value, list):
        return all(_finite_json(v) for v in value)
    return value is None or type(value) in (str, int, bool)


def validate_execution(execution):
    """Require complete, ordered execution provenance without comparing run identities."""
    errors = []
    if not isinstance(execution, dict):
        errors.append("missing execution provenance")
    else:
        if not isinstance(execution.get("run_id"), str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", execution["run_id"]):
            errors.append("missing or invalid run ID")
        for field in ("python_version", "platform"):
            if not isinstance(execution.get(field), str) or not execution[field].strip():
                errors.append(f"missing execution {field}")
        command = execution.get("command")
        if not isinstance(command, list) or not command or any(not isinstance(s, str) or not s for s in command):
            errors.append("missing execution command")
        try:
            start = datetime.fromisoformat(execution["started_at"])
            finish = datetime.fromisoformat(execution["finished_at"])
            if start.utcoffset() is None or finish.utcoffset() is None or finish < start:
                raise ValueError("timezone or ordering")
        except (KeyError, TypeError, ValueError):
            errors.append("invalid execution timestamps")
    return errors


def validate_record_metadata(record, base=None):
    """Validate provenance/lifecycle independently of a result's pass/fail value."""
    errors = []
    if not isinstance(record, dict):
        return ["executed record must be an object"]
    if type(record.get("schema_version")) is not int or record["schema_version"] != 2:
        errors.append("require evidence schema_version=2")
    errors.extend(validate_execution(record.get("execution")))
    if not isinstance(record.get("tool"), str) or not record["tool"].strip():
        errors.append("missing execution tool")
    if record.get("claim_support") != "sampled-reference-model-only":
        errors.append("unsupported claim scope")
    if record.get("review") not in ("pending", "reviewed"):
        errors.append("invalid review state")
    if record.get("review") == "reviewed":
        review = record.get("review_reference")
        if not isinstance(review, dict):
            errors.append("reviewed record requires a review reference")
        else:
            if not isinstance(review.get("reviewer"), str) or not review["reviewer"].strip():
                errors.append("missing reviewer identity")
            if not isinstance(review.get("artifact"), str) or not review["artifact"].strip():
                errors.append("missing review artifact")
            if not isinstance(review.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", review["sha256"]):
                errors.append("invalid review artifact hash")
            if base is None:
                errors.append("reviewed record requires an artifact base for integrity checking")
            else:
                try:
                    if hashlib.sha256(local_file(Path(base), review["artifact"]).read_bytes()).hexdigest() != review.get("sha256"):
                        errors.append("missing or stale review artifact")
                except (OSError, KeyError, TypeError, ValueError):
                    errors.append("missing or invalid review artifact")
    if record.get("acceptance") != "not_accepted_for_hardware":
        errors.append("reference-model evidence cannot assert hardware acceptance")
    return errors


def _check(data, base):
    errors = []
    required = ("sources", "requirements", "functions", "components", "interfaces", "verification", "evidence")
    maps, ids = {}, set()
    for group in (*required, "actors"):
        rows = data.get(group, [] if group == "actors" else None)
        if not isinstance(rows, list) or (group in required and not rows):
            errors.append(f"Missing/nonempty list required: {group}")
            maps[group] = {}
            continue
        maps[group] = {}
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
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

    if type(data.get("schema_version")) is not int or data["schema_version"] != 2:
        errors.append("Require baseline schema_version=2; v1 snapshots remain historical")
    if data.get("scope") != "illustrative-reference-model":
        errors.append("This checker supports the illustrative-reference-model scope only")
    for row in maps["sources"].values():
        try:
            source = local_file(base, row["artifact"])
            locator = row.get("locator")
            if not source.is_file():
                errors.append(f"{row['id']}: missing source artifact")
            elif not isinstance(locator, str) or not locator.strip() or source.read_text(encoding="utf-8").count(locator) != 1:
                errors.append(f"{row['id']}: source locator must identify one exact text occurrence")
        except (OSError, KeyError, TypeError, ValueError):
            errors.append(f"{row['id']}: invalid source artifact/locator")
    for row in maps["requirements"].values():
        link(row["id"], row.get("source"), "sources")
        links(row["id"], row.get("functions"), "functions")
        if row.get("status") != "proposed":
            errors.append(f"{row['id']}: this teaching schema requires proposed requirement status")
    for row in maps["functions"].values():
        links(row["id"], row.get("components"), "components")
    endpoints = set(maps["components"]) | set(maps["actors"])
    for row in maps["interfaces"].values():
        for end in ("from", "to"):
            if not isinstance(row.get(end), str) or row[end] not in endpoints:
                errors.append(f"{row['id']}: unresolved {end} component/actor {row.get(end)}")
    covered = set()
    for row in maps["verification"].values():
        values = row.get("requirements")
        links(row["id"], values, "requirements")
        if isinstance(values, list):
            covered.update(v for v in values if isinstance(v, str))
        link(row["id"], row.get("evidence"), "evidence")
    for requirement in maps["requirements"]:
        if requirement not in covered:
            errors.append(f"{requirement}: no planned verification")
    configuration = data.get("configuration_files")
    if not isinstance(configuration, list) or not configuration or any(not isinstance(p, str) or not p for p in configuration) or len(configuration) != len(set(configuration)):
        errors.append("Require unique nonempty configuration_files")
        configuration = []
    for source in maps["sources"].values():
        if source.get("artifact") not in configuration:
            errors.append(f"{source['id']}: source artifact absent from configuration coverage")
    if data.get("baseline_artifact") not in configuration:
        errors.append("Baseline artifact must be included in configuration coverage")

    outcomes, valid_records, rejected_records = {}, [], []
    reported_procedures = 0
    for row in maps["evidence"].values():
        owner, status = row["id"], row.get("status")
        if status not in ("planned", "drafted", "executed"):
            errors.append(f"{owner}: unsupported evidence status; review/acceptance are separate")
            continue
        if status == "planned":
            continue
        if status == "drafted":
            try:
                if not local_file(base, row["artifact"]).is_file():
                    errors.append(f"{owner}: drafted artifact does not exist")
            except (OSError, KeyError, TypeError, ValueError):
                errors.append(f"{owner}: invalid drafted artifact")
            continue
        first_error, candidate = len(errors), {}
        try:
            record = json.loads(local_file(base, row["artifact"]).read_text(encoding="utf-8"))
            errors.extend(f"{owner}: {e}" for e in validate_record_metadata(record, base))
            if not isinstance(record, dict):
                raise ValueError("record object")
            if row.get("scope") != data.get("scope") or record.get("scope") != row.get("scope"):
                errors.append(f"{owner}: evidence scope mismatch")
            if json.loads(local_file(base, data["baseline_artifact"]).read_text(encoding="utf-8")) != data:
                errors.append(f"{owner}: supplied baseline differs from its configured artifact")
            config = record.get("configuration")
            if not isinstance(config, dict) or not config or set(config) != set(configuration):
                errors.append(f"{owner}: incomplete configuration coverage")
            if isinstance(config, dict):
                execution = record.get("execution")
                if isinstance(execution, dict) and "loaded_sources" in execution:
                    expected_bindings = {name: digest for name, digest in config.items() if name.endswith(".py")}
                    if execution["loaded_sources"] != expected_bindings:
                        errors.append(f"{owner}: loaded-source bindings differ from Python configuration")
                for relative, digest in config.items():
                    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) or hashlib.sha256(local_file(base, relative).read_bytes()).hexdigest() != digest:
                        errors.append(f"{owner}: stale or invalid configuration {relative}")
            results = record.get("results")
            if not isinstance(results, list) or not results:
                errors.append(f"{owner}: missing executed outcomes")
            else:
                reported_procedures += len(results)
                for result in results:
                    if not isinstance(result, dict):
                        errors.append(f"{owner}: malformed outcome")
                        continue
                    ident = result.get("verification")
                    link(owner, ident, "verification")
                    if not isinstance(ident, str):
                        continue
                    if ident in candidate or ident in outcomes:
                        errors.append(f"Duplicate executed outcome: {ident}")
                    if result.get("result") not in ("pass", "fail", "inconclusive"):
                        errors.append(f"{ident}: invalid result")
                    if not isinstance(result.get("observed"), dict) or not result["observed"] or not _finite_json(result["observed"]):
                        errors.append(f"{ident}: require structured finite observations")
                    if ident in maps["verification"] and maps["verification"][ident].get("evidence") != owner:
                        errors.append(f"{ident}: outcome stored in the wrong evidence artifact")
                    candidate[ident] = result.get("result")
            expected = {r["id"] for r in maps["verification"].values() if r.get("evidence") == owner}
            for ident in expected - set(candidate):
                errors.append(f"{ident}: executed evidence has no outcome")
        except (OSError, ValueError, TypeError, KeyError, AttributeError):
            errors.append(f"{owner}: missing or malformed executed artifact/configuration")
        if len(errors) == first_error:
            valid_records.append(owner)
            outcomes.update(candidate)
        else:
            rejected_records.append(owner)

    # Valid execution can report failure. A passing result supports a requirement
    # only when all linked activities pass and the complete baseline is valid.
    passing = []
    if not errors:
        for requirement in maps["requirements"]:
            activities = [r["id"] for r in maps["verification"].values() if requirement in r.get("requirements", [])]
            if activities and all(outcomes.get(i) == "pass" for i in activities):
                passing.append(requirement)
    return errors, {
        "integrity": "invalid" if errors else "valid",
        "requirements": len(maps["requirements"]),
        "requirements_with_passing_model_evidence": len(passing),
        "reported_procedures": reported_procedures,
        "executed_procedures": len(outcomes),
        "passed_procedures": sum(v == "pass" for v in outcomes.values()),
        "failed_procedures": sum(v == "fail" for v in outcomes.values()),
        "inconclusive_procedures": sum(v == "inconclusive" for v in outcomes.values()),
        "valid_execution_records": valid_records,
        "rejected_execution_records": rejected_records,
        "scope": data.get("scope"),
        "claim_support": "not_established" if errors else "recorded-sampled-model-outcomes-only",
        "semantic_adequacy": "not_assessed",
        "acceptance": "not_assessed",
    }


def check(data, base):
    try:
        return _check(data, Path(base))
    except (KeyError, TypeError, ValueError, AttributeError) as error:
        return [f"Malformed baseline: {error}"], {"integrity": "invalid", "requirements_with_passing_model_evidence": 0, "executed_procedures": 0, "claim_support": "not_established", "acceptance": "not_assessed"}


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

"""Execute bounded gallery fault models using exact probabilities and exhaustive states.

The inputs describe authored, static AND/OR abstractions. Results establish their
logic and conditional scenario arithmetic, never measured reliability or acceptance.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import argparse
import datetime
import hashlib
import json
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("aerospace", "automotive", "defense", "medical-device", "electronic-systems")
LIMIT_EVENTS = 12
INDEPENDENCE = "mutually_independent_basic_events_with_shared_causes_explicitly_reused"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    raw = Path(path).read_bytes()
    if len(raw) > 2_000_000:
        raise ValueError("Model/result exceeds 2 MB bound")
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON number: " + value)))


def fraction(value):
    if not isinstance(value, str) or len(value) > 80:
        raise ValueError("Probabilities must be exact rational strings")
    result = Fraction(value)
    if not 0 <= result <= 1:
        raise ValueError("Probability outside [0,1]")
    return result


def validate_model(model):
    if not isinstance(model, dict) or model.get("schema_version") != 1 or model.get("scope") != "authored-static-fault-model":
        raise ValueError("Unsupported gallery model schema or scope")
    if model.get("probability_assumption") != INDEPENDENCE:
        raise ValueError("Explicit supported mutual-independence assumption required; correlation is not inferred")
    for field in ("id", "system", "hazard", "mission", "basis"):
        if not isinstance(model.get(field), str) or not model[field].strip():
            raise ValueError(f"Missing {field}")
    events, gates = model["events"], model["gates"]
    if not isinstance(events, dict) or not 1 <= len(events) <= LIMIT_EVENTS:
        raise ValueError(f"Require 1..{LIMIT_EVENTS} basic events")
    if not isinstance(gates, dict) or len(gates) > 64 or set(events) & set(gates):
        raise ValueError("Invalid or duplicate gate/event IDs")
    for event in events.values():
        if not event.get("description") or not event.get("basis"):
            raise ValueError("Event description and basis required")
        fraction(event["probability"])
    seen, active = set(), set()
    def visit(name, depth=0):
        if name in active or depth > 64:
            raise ValueError("Cycle or excessive gate depth")
        if name in events or name in seen:
            return
        if name not in gates:
            raise ValueError(f"Unknown event/gate: {name}")
        gate = gates[name]
        if gate.get("operator") not in {"and", "or"} or not isinstance(gate.get("inputs"), list) or not 1 <= len(gate["inputs"]) <= 32:
            raise ValueError(f"Unsupported gate: {name}")
        active.add(name)
        for child in gate["inputs"]:
            visit(child, depth + 1)
        active.remove(name)
        seen.add(name)
    for name in gates:
        visit(name)
    visit(model["top_event"])
    if not isinstance(model.get("scenarios"), list) or not 1 <= len(model["scenarios"]) <= 32:
        raise ValueError("Require 1..32 scenarios")
    if not isinstance(model.get("claims"), list) or not 1 <= len(model["claims"]) <= 64:
        raise ValueError("Require 1..64 claims")
    scenario_ids = set()
    for scenario in model["scenarios"]:
        if scenario["id"] in scenario_ids or not scenario.get("basis"):
            raise ValueError("Scenario IDs must be unique and have a basis")
        scenario_ids.add(scenario["id"])
        for name, value in scenario["overrides"].items():
            if name not in events:
                raise ValueError("Scenario refers to unknown event")
            fraction(value)
    if not scenario_ids:
        raise ValueError("At least one declared scenario required")
    claim_ids = set()
    for claim in model["claims"]:
        if claim["id"] in claim_ids or claim.get("expectation") not in {"holds", "counterexample"}:
            raise ValueError("Invalid claim identity or expectation")
        claim_ids.add(claim["id"])
        if type(claim.get("expected_top")) is not bool or not claim.get("description"):
            raise ValueError("A claim needs a Boolean conclusion and description")
        for name, value in claim["when"].items():
            if name not in events or type(value) is not bool:
                raise ValueError("Claim condition must name Boolean basic events")
    if not claim_ids:
        raise ValueError("At least one claim is required")


def evaluate(model, state, name=None):
    name = name or model["top_event"]
    if name in model["events"]:
        return state[name]
    gate = model["gates"][name]
    values = [evaluate(model, state, child) for child in gate["inputs"]]
    return all(values) if gate["operator"] == "and" else any(values)


def analyze(model):
    validate_model(model)
    names = sorted(model["events"])
    states = [dict(zip(names, values)) for values in product((False, True), repeat=len(names))]
    outcomes = [(state, evaluate(model, state)) for state in states]
    cuts = []
    for state, top in outcomes:
        if not top:
            continue
        failed = [name for name in names if state[name]]
        if all(not evaluate(model, {**state, name: False}) for name in failed):
            cuts.append(failed)
    cuts.sort(key=lambda cut: (len(cut), cut))
    scenarios = []
    for scenario in model["scenarios"]:
        probabilities = {name: fraction(event["probability"]) for name, event in model["events"].items()}
        probabilities.update({name: fraction(value) for name, value in scenario["overrides"].items()})
        probability = Fraction(0)
        for state, top in outcomes:
            if top:
                mass = Fraction(1)
                for name in names:
                    p = probabilities[name]
                    mass *= p if state[name] else 1 - p
                probability += mass
        scenarios.append({"id": scenario["id"], "basis": scenario["basis"],
                          "probability": str(probability), "decimal": float(probability),
                          "unit": "per_declared_demand", "overrides": scenario["overrides"]})
    claims = []
    for claim in model["claims"]:
        selected = [(state, top) for state, top in outcomes if all(state[key] == value for key, value in claim["when"].items())]
        failures = [state for state, top in selected if top != claim["expected_top"]]
        holds = bool(selected) and not failures
        expected = holds if claim["expectation"] == "holds" else bool(failures)
        claims.append({"id": claim["id"], "description": claim["description"], "expectation": claim["expectation"],
                       "property_holds": holds, "matched_assignments": len(selected), "counterexamples": len(failures),
                       "first_counterexample": failures[0] if failures else None,
                       "result": "pass" if expected else "fail"})
    return {"schema_version": 1, "model": model["id"], "hazard": model["hazard"],
            "scope": "exhaustive_static_boolean_and_conditional_probability",
            "mission": model["mission"], "basic_events": len(names), "completed_assignments": len(states),
            "hazard_assignments": sum(top for _, top in outcomes), "cut_sets_complete": True,
            "minimal_cut_sets": cuts, "scenarios": scenarios, "claims": claims,
            "probability_assumption": model["probability_assumption"],
            "parameter_status": "synthetic_scenario_inputs_not_measured_failure_rates",
            "physical_validation": "not_performed", "risk_acceptance": "not_assessed",
            "result": "pass" if all(c["result"] == "pass" for c in claims) else "fail"}


def model_paths(root=ROOT):
    return sorted(path for domain in DOMAINS for path in (root / "examples" / domain).glob("*/analysis/failure-model.json"))


def run(path):
    model = load_json(path)
    report = analyze(model)
    report["configuration"] = {"analysis/failure-model.json": digest(path),
                               "scripts/analyze_gallery.py": digest(Path(__file__))}
    for name in ("requirements.md", "architecture.md", "hazard-analysis.md"):
        report["configuration"][name] = digest(path.parents[1] / name)
    report["run_id"] = hashlib.sha256(json.dumps(report, sort_keys=True).encode()).hexdigest()[:20]
    return report


def render_report(model, report):
    lines = [f"# Executed model study: {model['system']}", "",
             f"Selected hazard: **{model['hazard']}**. Model: **{model['id']}**. Run: `{report['run_id']}`.", "",
             "## Engineering interpretation", "", model["interpretation"], "",
             "## Executed scope", "",
             f"Exhaustive enumeration evaluated **{report['completed_assignments']} Boolean states** over {report['basic_events']} declared events. It derived **{len(report['minimal_cut_sets'])} complete minimal cut sets** for the authored static model. This is exact static analysis, not a temporal or physical simulation.", "",
             model["mission"], "",
             "All numerical inputs below are synthetic scenario assumptions. The probability calculation assumes mutual independence of distinct basic events after shared causes have been represented as reused IDs. It sums disjoint complete assignments; it does not multiply repeated events twice or approximate a union by summing overlapping cut probabilities.", "",
             "## Complete minimal cut sets", "", "| Cut | Basic events |", "| --- | --- |"]
    lines += [f"| {index} | {', '.join(cut)} |" for index, cut in enumerate(report["minimal_cut_sets"], 1)]
    lines += ["", "## Conditional parameter scenarios", "", "| Scenario | Exact probability per declared demand | Decimal | Basis |", "| --- | --- | --- | --- |"]
    lines += [f"| {row['id']} | {row['probability']} | {row['decimal']:.8g} | {row['basis']} |" for row in report["scenarios"]]
    lines += ["", "## Checked claims and retained counterexamples", "",
              "A passing check can mean that an expected counterexample was found. It does not make the rejected engineering claim true.", "",
              "| Claim | Property holds in selected states? | States examined | Counterexamples | Check outcome |", "| --- | --- | --- | --- | --- |"]
    for row in report["claims"]:
        lines.append(f"| {row['description']} | {row['property_holds']} | {row['matched_assignments']} | {row['counterexamples']} | {row['result']} |")
    lines += ["", "## Evidence and next decisions", "",
              "- [Authored model and event basis](failure-model.json)",
              "- [Executed exact results, including counterexample states](../evidence/analysis/model-results.json)",
              "- [Independent CSE implementation cross-check](../evidence/analysis/cse-crosscheck.json)",
              "- [Requirements and proposed acceptance conditions](../requirements.md)",
              "- [Source/applicability review](../source-review.md)", "",
              "The CSE receipt compares a separate implementation's complete cuts and baseline exact probability; it is not independent engineering acceptance of the event model. Immutable run directories preserve the model, engine, source snapshots and result bytes. Physical rates, timing, control effectiveness, human performance, adopted standards and acceptance remain separate evidence obligations.", ""]
    return "\n".join(lines)


def cse_record(model):
    return {"version": "failure-analysis-1.0", "id": model["id"], "revision": "gallery-hardening-1",
            "basis": model["basis"], "events": model["events"], "gates": model["gates"],
            "top_event": model["top_event"], "probability": {
                "assumption": "mutually_independent", "basis": "Synthetic demand scenarios; shared causes are reused event IDs.",
                "mission": model["mission"]}, "fmea": {}}


def crosscheck(path, report, helper):
    model = load_json(path)
    cross_input = path.with_name("cse-failure-model.json")
    cross_input.write_text(json.dumps(cse_record(model), indent=2) + "\n", encoding="utf-8")
    command = [sys.executable, "-B", str(helper), str(cross_input), "--required", "fault_tree", "--required", "probability"]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError("CSE cross-check failed: " + (result.stderr or result.stdout))
    observed = json.loads(result.stdout)
    cuts = observed["checks"]["fault_tree"]["minimal_cut_sets"]
    probability = observed["checks"]["probability"]["probability"]
    base = next(s for s in report["scenarios"] if not s["overrides"])
    matches = cuts == report["minimal_cut_sets"] and probability == base["probability"]
    if not matches:
        raise ValueError("Independent CSE calculation disagrees")
    runtime = helper.resolve().parents[3]
    sources = [helper, runtime / "scripts/failure_analysis.py", runtime / "verifier/failure_analysis.py",
               runtime / "verifier/core.py", runtime / "verifier/foundation.py"]
    receipt = {"schema_version": 1, "scope": "independent_implementation_crosscheck_not_independent_engineering_review",
               "model_sha256": digest(path), "input_sha256": digest(cross_input),
               "helper_sources": {str(p): digest(p) for p in sources},
               "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "command": command, "matched": matches, "cse_result": observed}
    target = path.parents[1] / "evidence/analysis/cse-crosscheck.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", help="Gallery folder name")
    parser.add_argument("--check", action="store_true", help="Compare rerun results with saved evidence without writing")
    parser.add_argument("--cse-helper", type=Path, help="Explicit CSE failure-analysis entrypoint for an implementation cross-check")
    args = parser.parse_args()
    if args.check and args.cse_helper:
        parser.error("--check does not write cross-check receipts")
    paths = [p for p in model_paths() if not args.case or p.parents[1].name == args.case]
    if not paths:
        parser.error("No matching gallery models")
    summaries = []
    try:
        for path in paths:
            report = run(path)
            target = path.parents[1] / "evidence/analysis/model-results.json"
            if args.check:
                if load_json(target) != report:
                    raise ValueError(f"Stale or changed results: {target}")
                if path.with_name("report.md").read_text(encoding="utf-8") != render_report(load_json(path), report):
                    raise ValueError(f"Stale interpretation view: {path}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
                path.with_name("report.md").write_text(render_report(load_json(path), report), encoding="utf-8")
                execution = {"run_id": report["run_id"], "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                             "python": platform.python_version(), "command": "python3 scripts/analyze_gallery.py",
                             "result_sha256": digest(target), "scope": report["scope"]}
                run_dir = target.parent / "runs" / report["run_id"]
                run_dir.mkdir(parents=True, exist_ok=True)
                execution_path = run_dir / "execution.json"
                if not execution_path.exists():
                    execution_path.write_text(json.dumps(execution, indent=2) + "\n", encoding="utf-8")
                archived = {"model-results.json": target.read_bytes(), "failure-model.json": path.read_bytes(),
                            "analyze_gallery.py": Path(__file__).read_bytes()}
                for name in ("requirements.md", "architecture.md", "hazard-analysis.md"):
                    archived[name + ".snapshot"] = (path.parents[1] / name).read_bytes()
                for name, content in archived.items():
                    archive_path = run_dir / name
                    if archive_path.exists() and archive_path.read_bytes() != content:
                        raise ValueError(f"Immutable run archive collision: {archive_path}")
                    if not archive_path.exists():
                        archive_path.write_bytes(content)
                if args.cse_helper:
                    crosscheck(path, report, args.cse_helper)
            if report["result"] != "pass":
                raise ValueError(f"Expected model claim failed: {path}")
            summaries.append({"case": path.parents[1].name, "assignments": report["completed_assignments"],
                              "cut_sets": len(report["minimal_cut_sets"]), "claims": len(report["claims"])})
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as error:
        parser.exit(1, str(error) + "\n")
    print(json.dumps({"models": summaries, "physical_validation": "not_performed", "risk_acceptance": "not_assessed"}, indent=2))


if __name__ == "__main__":
    main()

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
import re
import subprocess
import sys
import tempfile

_LOADED_MODULE_CODE = sys._getframe().f_code

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("aerospace", "automotive", "defense", "medical-device", "electronic-systems")
LIMIT_EVENTS = 12
INDEPENDENCE = "mutually_independent_basic_events_with_shared_causes_explicitly_reused"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    if len(raw) > 2_000_000:
        raise ValueError("Model/result exceeds 2 MB bound")
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON number: " + value)))


def load_json(path):
    return parse_json(Path(path).read_bytes())


def bind_loaded_source(path, loaded_code):
    """Reject changed origins and stale bytecode, then bind the exact source bytes."""
    path = Path(path).resolve()
    if Path(loaded_code.co_filename).resolve() != path:
        raise ValueError(f"Loaded source origin differs: {path}")
    source = path.read_bytes()
    compiled = compile(source, loaded_code.co_filename, "exec", dont_inherit=True, optimize=sys.flags.optimize)
    if compiled != loaded_code:
        raise ValueError(f"Loaded code differs from source bytes: {path}")
    return hashlib.sha256(source).hexdigest()


_BOUND_ENGINE_SHA = bind_loaded_source(Path(__file__), _LOADED_MODULE_CODE)


def capture_configuration(path):
    paths = {"analysis/failure-model.json": path, "scripts/analyze_gallery.py": Path(__file__)}
    paths.update({name: path.parents[1] / name for name in ("requirements.md", "architecture.md", "hazard-analysis.md")})
    sources = {name: item.read_bytes() for name, item in paths.items()}
    hashes = {name: hashlib.sha256(content).hexdigest() for name, content in sources.items()}
    if hashes["scripts/analyze_gallery.py"] != _BOUND_ENGINE_SHA:
        raise ValueError("Source changed after import: scripts/analyze_gallery.py")
    return sources, hashes


def unchanged_configuration(path, expected):
    sources, actual = capture_configuration(path)
    if actual != expected:
        raise ValueError("Configuration changed during execution; no evidence published")
    return sources


def fraction(value):
    if not isinstance(value, str) or len(value) > 80 or not re.fullmatch(r"[-+]?\d+(?:/\d+|\.\d+)?", value):
        raise ValueError("Probabilities must be bounded exact rational or decimal strings (no exponents)")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"Invalid probability: {value}") from error
    if not 0 <= result <= 1:
        raise ValueError("Probability outside [0,1]")
    return result


def validate_model(model):
    if not isinstance(model, dict) or model.get("schema_version") != 1 or model.get("scope") != "authored-static-fault-model":
        raise ValueError("Unsupported gallery model schema or scope")
    if model.get("probability_assumption") != INDEPENDENCE:
        raise ValueError("Explicit supported mutual-independence assumption required; correlation is not inferred")
    for field in ("id", "system", "hazard", "mission", "basis", "interpretation"):
        if not isinstance(model.get(field), str) or not model[field].strip():
            raise ValueError(f"Missing {field}")
    events, gates = model.get("events"), model.get("gates")
    if not isinstance(events, dict) or not 1 <= len(events) <= LIMIT_EVENTS:
        raise ValueError(f"Require 1..{LIMIT_EVENTS} basic events")
    if not isinstance(gates, dict) or len(gates) > 64 or set(events) & set(gates):
        raise ValueError("Invalid or duplicate gate/event IDs")
    if any(not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,79}", name) for name in (*events, *gates)):
        raise ValueError("Event and gate IDs must be bounded named identifiers")
    for name, event in events.items():
        if not isinstance(event, dict) or any(not isinstance(event.get(field), str) or not event[field].strip() for field in ("description", "basis")):
            raise ValueError(f"Event {name} requires a description and basis")
        fraction(event.get("probability"))
    seen, active = set(), set()
    def visit(name, depth=0):
        if not isinstance(name, str):
            raise ValueError("Gate inputs and top_event must be named IDs")
        if name in active or depth > 64:
            raise ValueError("Cycle or excessive gate depth")
        if name in events or name in seen:
            return
        if name not in gates:
            raise ValueError(f"Unknown event/gate: {name}")
        gate = gates[name]
        if not isinstance(gate, dict) or gate.get("operator") not in {"and", "or"} or not isinstance(gate.get("inputs"), list) or not 1 <= len(gate["inputs"]) <= 32:
            raise ValueError(f"Unsupported gate: {name}")
        active.add(name)
        for child in gate["inputs"]:
            visit(child, depth + 1)
        active.remove(name)
        seen.add(name)
    for name in gates:
        visit(name)
    visit(model.get("top_event"))
    if not isinstance(model.get("scenarios"), list) or not 1 <= len(model["scenarios"]) <= 32:
        raise ValueError("Require 1..32 scenarios")
    if not isinstance(model.get("claims"), list) or not 1 <= len(model["claims"]) <= 64:
        raise ValueError("Require 1..64 claims")
    scenario_ids = set()
    for scenario in model["scenarios"]:
        if not isinstance(scenario, dict) or not isinstance(scenario.get("id"), str) or not scenario["id"].strip() or not isinstance(scenario.get("overrides"), dict):
            raise ValueError("Scenarios require a named ID and overrides object")
        if scenario["id"] in scenario_ids or not isinstance(scenario.get("basis"), str) or not scenario["basis"].strip():
            raise ValueError("Scenario IDs must be unique and have a basis")
        scenario_ids.add(scenario["id"])
        for name, value in scenario["overrides"].items():
            if name not in events:
                raise ValueError("Scenario refers to unknown event")
            fraction(value)
    if sum(not scenario["overrides"] for scenario in model["scenarios"]) != 1:
        raise ValueError("Exactly one baseline scenario with empty overrides is required")
    claim_ids = set()
    for claim in model["claims"]:
        if not isinstance(claim, dict) or not isinstance(claim.get("id"), str) or not claim["id"].strip() or not isinstance(claim.get("when"), dict):
            raise ValueError("Claims require a named ID and when object")
        if claim["id"] in claim_ids or claim.get("expectation") not in {"holds", "counterexample"}:
            raise ValueError("Invalid claim identity or expectation")
        claim_ids.add(claim["id"])
        if type(claim.get("expected_top")) is not bool or not isinstance(claim.get("description"), str) or not claim["description"].strip():
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
    sources, configuration = capture_configuration(path)
    model = parse_json(sources["analysis/failure-model.json"])
    report = analyze(model)
    unchanged_configuration(path, configuration)
    report["configuration"] = configuration
    report["loaded_sources"] = {"scripts/analyze_gallery.py": _BOUND_ENGINE_SHA}
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
    sources = unchanged_configuration(path, report["configuration"])
    model = parse_json(sources["analysis/failure-model.json"])
    cross_input = path.with_name("cse-failure-model.json")
    cross_input.write_text(json.dumps(cse_record(model), indent=2) + "\n", encoding="utf-8")
    helper = helper.resolve()
    runtime = helper.parents[3]
    helper_paths = [helper, runtime / "scripts/failure_analysis.py", runtime / "verifier/failure_analysis.py",
                    runtime / "verifier/core.py", runtime / "verifier/foundation.py"]
    helper_hashes = {str(p): digest(p) for p in helper_paths}
    input_hash = digest(cross_input)
    # -B alone still reads caches. An empty unique prefix also excludes stale caches.
    with tempfile.TemporaryDirectory(prefix=".cse-cache-", dir=path.parent) as cache:
        command = [sys.executable, "-B", "-X", "pycache_prefix=" + cache, str(helper), str(cross_input),
                   "--required", "fault_tree", "--required", "probability"]
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
    unchanged_configuration(path, report["configuration"])
    if input_hash != digest(cross_input) or observed.get("input_sha256") != input_hash:
        raise ValueError("CSE input changed during cross-check")
    if helper_hashes != {str(p): digest(p) for p in helper_paths}:
        raise ValueError("CSE helper source changed during cross-check")
    receipt = {"schema_version": 1, "scope": "independent_implementation_crosscheck_not_independent_engineering_review",
               "model_sha256": report["configuration"]["analysis/failure-model.json"], "input_sha256": input_hash,
               "helper_sources": helper_hashes, "helper_entrypoint": str(helper),
               "helper_source_hash_scope": "observed_before_and_after_execution_not_loaded_module_binding",
               "bytecode_cache_policy": "fresh_empty_prefix_with_writes_disabled",
               "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "python": platform.python_version(), "command": command, "matched": matches, "cse_result": observed}
    target = path.parents[1] / "evidence/analysis/cse-crosscheck.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    previous = target.read_bytes() if target.exists() else None
    content = (json.dumps(receipt, indent=2) + "\n").encode()
    for raw in (previous, content):
        if raw is not None:
            archive = target.parent / "cse-runs" / (hashlib.sha256(raw).hexdigest() + ".json")
            archive.parent.mkdir(exist_ok=True)
            if archive.exists() and archive.read_bytes() != raw:
                raise ValueError("CSE receipt archive collision")
            if not archive.exists():
                archive.write_bytes(raw)
    target.write_bytes(content)


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
            sources = unchanged_configuration(path, report["configuration"])
            model = parse_json(sources["analysis/failure-model.json"])
            target = path.parents[1] / "evidence/analysis/model-results.json"
            if args.check:
                if load_json(target) != report:
                    raise ValueError(f"Stale or changed results: {target}")
                if path.with_name("report.md").read_text(encoding="utf-8") != render_report(model, report):
                    raise ValueError(f"Stale interpretation view: {path}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                content = (json.dumps(report, indent=2) + "\n").encode()
                execution = {"schema_version": 1, "run_id": report["run_id"], "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                             "python": platform.python_version(), "command": list(sys.orig_argv),
                             "entrypoint": str(Path(__file__).resolve()), "loaded_sources": report["loaded_sources"],
                             "result_sha256": hashlib.sha256(content).hexdigest(), "scope": report["scope"]}
                run_dir = target.parent / "runs" / report["run_id"]
                run_dir.mkdir(parents=True, exist_ok=True)
                execution_path = run_dir / "execution.json"
                if not execution_path.exists():
                    execution_path.write_text(json.dumps(execution, indent=2) + "\n", encoding="utf-8")
                archived = {"model-results.json": content, "failure-model.json": sources["analysis/failure-model.json"],
                            "analyze_gallery.py": sources["scripts/analyze_gallery.py"]}
                for name in ("requirements.md", "architecture.md", "hazard-analysis.md"):
                    archived[name + ".snapshot"] = sources[name]
                for name, content in archived.items():
                    archive_path = run_dir / name
                    if archive_path.exists() and archive_path.read_bytes() != content:
                        raise ValueError(f"Immutable run archive collision: {archive_path}")
                    if not archive_path.exists():
                        archive_path.write_bytes(content)
                unchanged_configuration(path, report["configuration"])
                target.write_bytes(archived["model-results.json"])
                path.with_name("report.md").write_text(render_report(model, report), encoding="utf-8")
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

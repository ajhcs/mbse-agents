"""Execution provenance and append-only records for the local reference example."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import platform
import re
import tempfile
import uuid
import sys

_LOADED_MODULE_CODE = sys._getframe().f_code


def bind_loaded_sources(base, modules):
    """Bind source bytes to the module code that Python actually executed.

    Comparing compiled code also rejects stale bytecode caches or a file change
    between Python reading a module and this binding being established. Later
    execution requires the exact bound bytes, including non-code changes.
    """
    bound = {}
    for name, loaded_code in modules.items():
        path = (base / name).resolve()
        if not path.is_relative_to(base.resolve()) or Path(loaded_code.co_filename).resolve() != path:
            raise ValueError(f"Loaded source origin differs from configuration: {name}")
        source = path.read_bytes()
        compiled = compile(source, loaded_code.co_filename, "exec", dont_inherit=True, optimize=sys.flags.optimize)
        if compiled != loaded_code:
            raise ValueError(f"Loaded code differs from source bytes: {name}")
        bound[name] = hashlib.sha256(source).hexdigest()
    return bound


def capture(base, exercise, command, *, loaded_sources=None):
    start = datetime.now(timezone.utc)
    files = json.loads((base / "baseline.json").read_text(encoding="utf-8"))["configuration_files"]
    configuration = {}
    for name in files:
        path = (base / name).resolve()
        if not path.is_relative_to(base.resolve()):
            raise ValueError(f"Configuration escapes baseline: {name}")
        configuration[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    python_sources = {name for name in configuration if name.endswith(".py")}
    if python_sources and loaded_sources is None:
        raise ValueError("Configured Python sources require loaded-source bindings")
    if loaded_sources is not None:
        if set(loaded_sources) != python_sources:
            raise ValueError("Loaded source bindings do not cover the configured Python files")
        changed = [name for name, digest in loaded_sources.items() if configuration.get(name) != digest]
        if changed:
            raise ValueError("Source changed after import: " + ", ".join(changed))
    results = exercise()
    finish = datetime.now(timezone.utc)
    # Reject a source change during execution, even if a result happened to pass.
    if any(hashlib.sha256((base / name).read_bytes()).hexdigest() != digest for name, digest in configuration.items()):
        raise ValueError("Configuration changed during execution; no record selected")
    return {
        "schema_version": 2,
        "scope": "illustrative-reference-model",
        "execution": {
            "run_id": start.strftime("%Y%m%dT%H%M%S.%fZ-") + uuid.uuid4().hex[:12],
            "started_at": start.isoformat(),
            "finished_at": finish.isoformat(),
            "command": list(command),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "loaded_sources": dict(loaded_sources or {}),
        },
        "tool": f"Python {platform.python_version()}",
        "configuration": configuration,
        "results": results,
        "claim_support": "sampled-reference-model-only",
        "acceptance": "not_accepted_for_hardware",
        "review": "pending",
    }


def _immutable(path, content):
    if path.is_symlink():
        raise ValueError(f"Refusing a symbolic-link evidence file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError:
        if path.read_bytes() != content:
            raise ValueError(f"Refusing to replace archived evidence: {path}")


def _archive_name(content):
    try:
        run_id = json.loads(content)["execution"]["run_id"]
        if isinstance(run_id, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", run_id):
            return run_id + ".json"
    except (KeyError, TypeError, ValueError):
        pass
    return "legacy-" + hashlib.sha256(content).hexdigest() + ".json"


def save(base, record, output=None, *, selection="results.json"):
    """Archive before replacing the selected record; explicit outputs never overwrite."""
    content = (json.dumps(record, indent=2, allow_nan=False) + "\n").encode("utf-8")
    archive = base / "evidence/runs" / _archive_name(content)
    if not archive.resolve().is_relative_to(base.resolve()):
        raise ValueError("Evidence archive escapes its example directory")
    if output is not None:
        output = Path(output)
        if output.exists():
            raise ValueError(f"Explicit output already exists: {output}")
        _immutable(archive, content)
        _immutable(output, content)
        return archive
    if not isinstance(selection, str) or Path(selection).name != selection or not selection.endswith(".json"):
        raise ValueError("Selection must be a JSON filename within the evidence directory")
    selected = base / "evidence" / selection
    if selected.is_symlink() or not selected.resolve().is_relative_to(base.resolve()):
        raise ValueError("Evidence selection is a symbolic link or escapes its example directory")
    if selected.exists():
        previous = selected.read_bytes()
        _immutable(base / "evidence/runs" / _archive_name(previous), previous)
    _immutable(archive, content)
    with tempfile.NamedTemporaryFile(dir=selected.parent, prefix=".selected-", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    try:
        os.replace(temporary, selected)
    finally:
        temporary.unlink(missing_ok=True)
    return archive


def compare(saved, actual):
    # A fresh reproduction has its own run ID, date and host. It must reproduce
    # the recorded configuration and observations, not invent a historical run.
    if not isinstance(saved, dict):
        return ["record must be an object"]
    fields = ("schema_version", "scope", "configuration", "results", "claim_support", "acceptance")
    errors = [field for field in fields if saved.get(field) != actual.get(field)]
    execution = saved.get("execution")
    if not isinstance(execution, dict) or execution.get("loaded_sources") != actual["execution"]["loaded_sources"]:
        errors.append("missing or mismatched loaded-source bindings")
    return errors

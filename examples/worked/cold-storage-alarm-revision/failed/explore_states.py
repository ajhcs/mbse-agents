"""Exhaust the sampled model's finite state abstraction against a counter oracle."""
from collections import deque
from copy import deepcopy


def explore(alarm_type, fault_delay_ms=1000):
    """Check every reachable abstract state and all 6 input-class/ack combinations.

    Absolute time is quotiented by translation; elapsed timers saturate after
    their decision threshold. Temperature classes are below 8, at/above 8, and
    invalid. Event history is observed per transition, not stored in state.
    This is a finite executable equivalence check, not physical validation.
    """
    high_limit, fault_limit = 21, fault_delay_ms // 100 + 1
    inputs = (("low", 7.9), ("high", 8), ("invalid", None))
    queue = deque([(alarm_type(), (False, 0, 0), [])])
    visited, transitions = set(), 0
    while queue:
        model, oracle, history = queue.popleft()
        now = model.last_ms if model.last_ms is not None else 0
        signature = (oracle, model.high, model.sensor_fault,
                     None if model.high_since is None else min(now - model.high_since, 2000),
                     None if model.invalid_since is None else min(now - model.invalid_since, fault_delay_ms),
                     model.last_ms is None)
        if signature in visited:
            continue
        visited.add(signature)
        if len(visited) > 10000:
            return False, {"reason": "state limit exceeded", "states": len(visited), "transitions": transitions}
        for label, temperature in inputs:
            for ack in (False, True):
                high, high_ticks, invalid_ticks = oracle
                old_pair = (high, invalid_ticks >= fault_limit)
                if label == "high":
                    high_ticks, invalid_ticks = min(high_ticks + 1, high_limit), 0
                    high = high or high_ticks >= high_limit
                elif label == "low":
                    high_ticks, invalid_ticks = 0, 0
                    high = high and not ack
                else:
                    high_ticks, invalid_ticks = 0, min(invalid_ticks + 1, fault_limit)
                fault = invalid_ticks >= fault_limit
                expected = {"high": high, "sensor_fault": fault, "local_alarm": high or fault}
                candidate = deepcopy(model)
                candidate.events = []
                tick = 0 if candidate.last_ms is None else candidate.last_ms + 100
                actual = candidate.step(tick, temperature, ack)
                events = [] if old_pair == (high, fault) else [{"time_ms": tick, "high": high, "sensor_fault": fault}]
                transitions += 1
                sequence = history + [{"input": label, "acknowledge": ack}]
                if actual != expected or candidate.events != events:
                    return False, {"states": len(visited), "transitions": transitions,
                                   "counterexample": sequence, "time_ms": tick,
                                   "expected": expected, "actual": actual,
                                   "expected_events": events, "actual_events": candidate.events}
                queue.append((candidate, (high, high_ticks, invalid_ticks), sequence))
    return True, {"states": len(visited), "transitions": transitions,
                  "input_combinations_per_state": 6, "counterexamples": 0,
                  "temperature_classes": ["below 8", "at/above 8", "invalid"],
                  "fault_delay_ms": fault_delay_ms, "time_quantum_ms": 100,
                  "abstraction": "time translation; timers saturated after decision thresholds; per-transition event checks"}


def check_inputs(alarm_type, fault_delay_ms=1000):
    failures, checked = [], 0
    invalid = (("none", None), ("nan", float("nan")), ("positive infinity", float("inf")),
               ("negative infinity", -float("inf")), ("string", "8"), ("boolean", True),
               ("mapping", {}), ("list", []))
    for label, temperature in invalid:
        model = alarm_type()
        for tick in range(0, fault_delay_ms + 100, 100):
            state = model.step(tick, temperature)
        checked += 1
        if not state["sensor_fault"] or state["high"]:
            failures.append(label)
    for tick in (0, -100, 200, 1, 100.0, True, "100", None):
        model = alarm_type()
        model.step(0, 7)
        before = deepcopy(model)
        checked += 1
        try:
            model.step(tick, 7)
            failures.append(f"accepted time {tick!r}")
        except ValueError:
            if model != before:
                failures.append(f"changed state on rejected time {tick!r}")
    model = alarm_type()
    checked += 1
    try:
        model.step(0, 7, "yes")
        failures.append("accepted nonboolean acknowledgement")
    except ValueError:
        pass
    return not failures, {"checked_cases": checked, "invalid_temperature_classes": len(invalid), "failures": failures}

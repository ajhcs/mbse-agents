"""Sampled clamp-release design study; no fluid/mechanical plant is modeled."""
from dataclasses import dataclass


@dataclass
class Clamp:
    closing_ms: int = 300
    last_ms: int = 0
    last_service_ms: int = 0
    release_ms: int | None = None
    closed: bool = False
    latched: bool = False

    def __post_init__(self):
        if type(self.closing_ms) is not int or self.closing_ms < 0 or self.closing_ms % 100:
            raise ValueError("Closing delay must be nonnegative integer 100 ms ticks")

    def step(self, time_ms, *, door_open=False, power=True, cpu_services=True,
             manual_rearm=False, interlock_failed=False, jammed=False):
        if type(time_ms) is not int or time_ms != self.last_ms + 100:
            raise ValueError("Model requires contiguous integer 100 ms ticks after time zero")
        values = (door_open, power, cpu_services, manual_rearm, interlock_failed, jammed)
        if any(type(value) is not bool for value in values):
            raise ValueError("Inputs must be Boolean")
        if cpu_services and power:
            self.last_service_ms = time_ms
        watchdog = time_ms - self.last_service_ms >= 200
        release = not power or (door_open and not interlock_failed) or watchdog
        if release and not self.latched:
            self.release_ms = time_ms
            self.latched = True
        if self.latched and not jammed and time_ms - self.release_ms >= self.closing_ms:
            self.closed = True
        if manual_rearm and self.closed and power and not door_open and cpu_services and not watchdog and not jammed:
            self.latched = False
            self.release_ms = None
            self.closed = False
        self.last_ms = time_ms
        return {"time_ms": time_ms, "release_ms": self.release_ms, "latched": self.latched,
                "closed": self.closed, "watchdog": watchdog, "hold_open": not self.latched,
                "powered_drive_permitted": power and not door_open and not watchdog and not self.latched}

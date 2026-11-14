"""Illustrative sampled alarm model; not deployed firmware or physical validation."""
from dataclasses import dataclass, field
import math


@dataclass
class Alarm:
    high: bool = False
    sensor_fault: bool = False
    high_since: int | None = None
    invalid_since: int | None = None
    last_ms: int | None = None
    events: list = field(default_factory=list)

    def step(self, time_ms, temperature_c, acknowledge=False):
        if type(time_ms) is not int or time_ms < 0 or time_ms % 100:
            raise ValueError("Model uses nonnegative integer 100 ms ticks")
        if self.last_ms is not None and time_ms - self.last_ms != 100:
            raise ValueError("Model requires contiguous 100 ms ticks")
        if type(acknowledge) is not bool:
            raise ValueError("Acknowledge must be boolean")
        previous = (self.high, self.sensor_fault)
        valid = type(temperature_c) in (int, float) and math.isfinite(temperature_c)
        if valid:
            self.invalid_since = None
            self.sensor_fault = False
            if temperature_c >= 8:
                if self.high_since is None:
                    self.high_since = time_ms
                if time_ms - self.high_since >= 2000:
                    self.high = True
            else:
                self.high_since = None
                if acknowledge:
                    self.high = False
        else:
            self.high_since = None
            if self.invalid_since is None:
                self.invalid_since = time_ms
            self.sensor_fault = time_ms - self.invalid_since >= 1000
        self.last_ms = time_ms
        if previous != (self.high, self.sensor_fault):
            self.events.append({"time_ms": time_ms, "high": self.high, "sensor_fault": self.sensor_fault})
        return {"high": self.high, "sensor_fault": self.sensor_fault,
                "local_alarm": self.high or self.sensor_fault}

# Greenhouse vent controller draft

The reviewable package is [requirements.md](requirements.md), [architecture.md](architecture.md), and [verification.md](verification.md). N-01–N-04 are preserved and traced into draft behavior, allocations, interfaces and planned evidence.

The design proposes a local driver-inhibit path, a local fault indication and latched recovery. Sample continuity/freshness, physical stopping time, recovery authority, remote-access scope, travel and weather behavior still need decisions. The unsupported 50 ms proposal is not a baseline requirement. No controller test was executed; no safety, reliability or acceptance claim is made.

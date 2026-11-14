# Preserved failed execution

The requirement and oracle now require a 500 ms invalid-reading interval, while
the implementation still waits 1000 ms. The recorded VER-03, VER-06, VER-07 and
VER-08 failures are intentional retained observations. `python3 -B run_checks.py
--check` reproduces them and exits 1; this is not a corrupted evidence record.
The repaired implementation is one directory above this snapshot.

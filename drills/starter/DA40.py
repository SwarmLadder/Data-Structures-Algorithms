"""DA40 — Rollback union–find (independent)

Process ops on n singletons: ['union', a, b], ['same', a, b] (record True/False), or
['undo'] (revert the most recent union that actually merged two sets; no-op if
none). Return the recorded answers. Use union by size without path compression.

Check: python -m tools.drills check DA40
Hints: python -m tools.drills hint DA40 1
"""

def solve(n, ops):
    raise NotImplementedError("Implement solve")

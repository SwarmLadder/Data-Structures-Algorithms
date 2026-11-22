"""DA47 — Makespan with k workers (independent)

Independent tasks with the given durations are assigned in input order, each to the
worker that becomes free earliest (ties: lowest worker id). Return the time when the
last task finishes (0 for no tasks).

Check: python -m tools.drills check DA47
Hints: python -m tools.drills hint DA47 1
"""

import heapq

def solve(durations, k):
    raise NotImplementedError("Implement solve")

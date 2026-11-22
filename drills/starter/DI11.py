"""DI11 — LRU cache simulator (independent)

Simulate an LRU cache with the given capacity. ops is a list of ['put', key, value]
or ['get', key]. Return the results of every get in order (-1 for a miss). A get
refreshes recency.

Check: python -m tools.drills check DI11
Hints: python -m tools.drills hint DI11 1
"""

from collections import OrderedDict

def solve(capacity, ops):
    raise NotImplementedError("Implement solve")

"""DI39 — Autocomplete top three (independent)

For each prefix of query (query[:1], query[:2], …), return up to three words from
words that start with it, in lexicographic order.

Check: python -m tools.drills check DI39
Hints: python -m tools.drills hint DI39 1
"""

from bisect import bisect_left

def solve(words, query):
    raise NotImplementedError("Implement solve")

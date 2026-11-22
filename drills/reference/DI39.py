"""DI39 reference: Autocomplete top three. Open after your own attempt."""
from bisect import bisect_left

def solve(words, query):
    words = sorted(words)
    out = []
    for i in range(1, len(query) + 1):
        prefix = query[:i]
        start = bisect_left(words, prefix)
        out.append([w for w in words[start:start + 3] if w.startswith(prefix)])
    return out

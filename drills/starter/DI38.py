"""DI38 — Trie: which queries are prefixes? (guided)

Insert every word into a trie (nested dicts), then return a list of booleans: for
each query, whether some word starts with it.

Check: python -m tools.drills check DI38
Hints: python -m tools.drills hint DI38 1
"""

___ = None  # replace every ___ below with your code

def solve(words, queries):
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, ___)
    out = []
    for q in queries:
        node = root
        ok = True
        for ch in q:
            if ch not in node:
                ok = False
                break
            node = ___
        out.append(ok)
    return out

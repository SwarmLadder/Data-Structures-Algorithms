"""Reference answer for B02. See the problem statement before reading.
"""
def solve(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        groups[''.join(sorted(word))].append(word)
    return sorted((sorted(g) for g in groups.values()), key=lambda g: g[0])

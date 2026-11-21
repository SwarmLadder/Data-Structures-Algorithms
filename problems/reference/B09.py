"""Reference answer for B09. See the problem statement before reading.
"""
def solve(labels, k):
    from collections import Counter
    counts = Counter(labels)
    return sorted(counts, key=lambda x: (-counts[x], x))[:k]

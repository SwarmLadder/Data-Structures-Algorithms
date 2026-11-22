"""DB39 reference: Top k frequent words. Open after your own attempt."""
def solve(words, k):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]

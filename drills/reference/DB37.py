"""DB37 reference: Sort by length, then alphabetically. Open after your own attempt."""
def solve(words):
    return sorted(words, key=lambda w: (len(w), w))

"""DB02 reference: Count words. Open after your own attempt."""
def solve(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

"""DI37 reference: Longest common prefix. Open after your own attempt."""
def solve(words):
    if not words:
        return ""
    for i, ch in enumerate(words[0]):
        if any(i >= len(w) or w[i] != ch for w in words[1:]):
            return words[0][:i]
    return words[0]

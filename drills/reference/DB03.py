"""DB03 reference: First repeated character. Open after your own attempt."""
def solve(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return ""

"""Reference answer for I01. See the problem statement before reading.
"""
def solve(text):
    last = {}
    start = best = 0
    for right, char in enumerate(text):
        if char in last and last[char] >= start:
            start = last[char] + 1
        last[char] = right
        best = max(best, right - start + 1)
    return best

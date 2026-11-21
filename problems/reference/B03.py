"""Reference answer for B03. See the problem statement before reading.
"""
def solve(text):
    from collections import Counter
    counts = Counter(text)
    for i, char in enumerate(text):
        if counts[char] == 1:
            return i
    return -1

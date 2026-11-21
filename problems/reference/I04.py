"""Reference answer for I04. See the problem statement before reading.
"""
def solve(text, k):
    if k == 0:
        return 0
    from collections import defaultdict
    count = defaultdict(int)
    left = best = 0
    for right, char in enumerate(text):
        count[char] += 1
        while len(count) > k:
            old = text[left]
            count[old] -= 1
            if count[old] == 0:
                del count[old]
            left += 1
        best = max(best, right - left + 1)
    return best

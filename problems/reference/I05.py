"""Reference answer for I05. See the problem statement before reading.
"""
def solve(intervals):
    merged = []
    for a, b in sorted(intervals):
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a,b])
    return merged

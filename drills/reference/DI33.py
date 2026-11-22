"""DI33 reference: Most non-overlapping meetings. Open after your own attempt."""
def solve(intervals):
    count, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):
        if start >= last_end:
            count += 1
            last_end = end
    return count

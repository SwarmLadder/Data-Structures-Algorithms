"""DI08 reference: Longest balanced binary subarray. Open after your own attempt."""
def solve(bits):
    first = {0: -1}
    total = best = 0
    for i, b in enumerate(bits):
        total += 1 if b else -1
        if total in first:
            best = max(best, i - first[total])
        else:
            first[total] = i
    return best

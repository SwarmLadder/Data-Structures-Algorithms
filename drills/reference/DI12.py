"""DI12 reference: Free time across schedules. Open after your own attempt."""
def solve(busy):
    merged = []
    for s, e in sorted(busy):
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return [[a[1], b[0]] for a, b in zip(merged, merged[1:])]

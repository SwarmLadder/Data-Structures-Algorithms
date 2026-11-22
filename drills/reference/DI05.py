"""DI05 reference: Running totals. Open after your own attempt."""
def solve(nums):
    out, total = [], 0
    for x in nums:
        total += x
        out.append(total)
    return out

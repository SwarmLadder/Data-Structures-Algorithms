"""DI45 reference: Pick the technique. Open after your own attempt."""
def solve(n, all_positive):
    if n <= 50:
        return "brute force"
    return "sliding window" if all_positive else "prefix sums"

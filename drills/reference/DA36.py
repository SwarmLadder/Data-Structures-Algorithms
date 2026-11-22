"""DA36 reference: Which structure?. Open after your own attempt."""
def solve(has_updates, combine):
    if not has_updates:
        return "prefix sums"
    if combine in ("sum", "xor"):
        return "fenwick"
    return "segment tree"

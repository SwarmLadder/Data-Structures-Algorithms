"""DA30 reference: Count coin combinations. Open after your own attempt."""
def solve(amount, coins):
    ways = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            ways[a] += ways[a - c]
    return ways[amount]

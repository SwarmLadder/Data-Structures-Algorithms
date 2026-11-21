"""Reference answer for A11. See the problem statement before reading.
"""
def solve(upgrades, budget):
    dp = [0] * (budget + 1)
    for cost,value in upgrades:
        for cap in range(budget,cost-1,-1):
            dp[cap] = max(dp[cap], dp[cap-cost]+value)
    return dp[budget]

"""Reference answer for A07. See the problem statement before reading.
"""
def solve(sizes, target):
    limit = target + 1
    dp = [limit] * (target + 1)
    dp[0] = 0
    for total in range(1, target + 1):
        for size in sizes:
            if size <= total:
                dp[total] = min(dp[total], dp[total-size]+1)
    return -1 if dp[target] == limit else dp[target]

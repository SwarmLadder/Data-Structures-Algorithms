"""DA28 reference: Longest palindromic subsequence. Open after your own attempt."""
def solve(s):
    n = len(s)
    if n == 0:
        return 0
    best = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        best[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                best[i][j] = best[i + 1][j - 1] + 2
            else:
                best[i][j] = max(best[i + 1][j], best[i][j - 1])
    return best[0][n - 1]

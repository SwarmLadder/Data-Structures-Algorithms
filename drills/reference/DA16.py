"""DA16 reference: Palindrome partitions. Open after your own attempt."""
def solve(s):
    out, parts = [], []
    def dfs(start):
        if start == len(s):
            out.append(parts.copy())
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                parts.append(piece)
                dfs(end)
                parts.pop()
    dfs(0)
    return out

"""DI41 reference: All subsets. Open after your own attempt."""
def solve(nums):
    out, chosen = [], []
    def dfs(i):
        if i == len(nums):
            out.append(chosen.copy())
            return
        dfs(i + 1)
        chosen.append(nums[i])
        dfs(i + 1)
        chosen.pop()
    dfs(0)
    return out

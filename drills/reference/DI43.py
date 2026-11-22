"""DI43 reference: Subsets without duplicates. Open after your own attempt."""
def solve(nums):
    nums = sorted(nums)
    out, path = [], []
    def dfs(start):
        out.append(path.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return sorted(out)

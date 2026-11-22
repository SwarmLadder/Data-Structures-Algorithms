"""DB27 reference: All permutations. Open after your own attempt."""
def solve(nums):
    out, current, used = [], [], [False] * len(nums)
    def dfs():
        if len(current) == len(nums):
            out.append(current.copy())
            return
        for i, value in enumerate(nums):
            if not used[i]:
                used[i] = True
                current.append(value)
                dfs()
                current.pop()
                used[i] = False
    dfs()
    return out

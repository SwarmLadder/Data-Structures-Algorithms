"""DI35 reference: Jump game. Open after your own attempt."""
def solve(nums):
    if not nums:
        return False
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True

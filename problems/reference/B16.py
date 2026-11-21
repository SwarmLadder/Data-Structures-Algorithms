"""Reference answer for B16. See the problem statement before reading.
"""
def solve(nums):
    result = [1] * len(nums)
    left = 1
    for i, x in enumerate(nums):
        result[i] = left
        left *= x
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

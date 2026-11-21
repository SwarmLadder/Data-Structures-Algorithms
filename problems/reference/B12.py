"""Reference answer for B12. See the problem statement before reading.
"""
def solve(nums):
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

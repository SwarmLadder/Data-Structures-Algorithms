"""DB41 reference: The value without a partner. Open after your own attempt."""
def solve(nums):
    answer = 0
    for x in nums:
        answer ^= x
    return answer

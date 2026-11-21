"""Reference answer for I03. See the problem statement before reading.
"""
def solve(nums, target):
    from collections import defaultdict
    freq = defaultdict(int)
    freq[0] = 1
    prefix = answer = 0
    for x in nums:
        prefix += x
        answer += freq[prefix - target]
        freq[prefix] += 1
    return answer

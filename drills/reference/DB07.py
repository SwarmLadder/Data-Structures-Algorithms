"""DB07 reference: Remove duplicates from a sorted list. Open after your own attempt."""
def solve(nums):
    write = 0
    for read in range(len(nums)):
        if write == 0 or nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write

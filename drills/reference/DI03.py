"""DI03 reference: Longest run with at most k flips. Open after your own attempt."""
def solve(bits, k):
    left = zeros = best = 0
    for right, b in enumerate(bits):
        zeros += b == 0
        while zeros > k:
            zeros -= bits[left] == 0
            left += 1
        best = max(best, right - left + 1)
    return best

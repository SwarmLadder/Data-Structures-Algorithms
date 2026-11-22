"""DB40 reference: Count inversions. Open after your own attempt."""
def solve(nums):
    def sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, x = sort(a[:mid])
        right, y = sort(a[mid:])
        out, i, j, count = [], 0, 0, x + y
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
                count += len(left) - i
        return out + left[i:] + right[j:], count
    return sort(nums)[1]

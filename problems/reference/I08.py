"""Reference answer for I08. See the problem statement before reading.
"""
def solve(nums, k):
    import heapq
    heap = []
    for x in set(nums):
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]

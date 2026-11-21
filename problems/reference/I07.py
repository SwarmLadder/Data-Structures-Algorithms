"""Reference answer for I07. See the problem statement before reading.
"""
def solve(jobs):
    import heapq
    ends = []
    answer = 0
    for start, end in sorted(jobs):
        while ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
        answer = max(answer, len(ends))
    return answer

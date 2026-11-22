"""DI10 reference: Minimum meeting rooms. Open after your own attempt."""
import heapq

def solve(meetings):
    ends = []
    for start, end in sorted(meetings):
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)
    return len(ends)

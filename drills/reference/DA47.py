"""DA47 reference: Makespan with k workers. Open after your own attempt."""
import heapq

def solve(durations, k):
    heap = [(0, w) for w in range(k)]
    finish = 0
    for d in durations:
        t, w = heapq.heappop(heap)
        finish = max(finish, t + d)
        heapq.heappush(heap, (t + d, w))
    return finish

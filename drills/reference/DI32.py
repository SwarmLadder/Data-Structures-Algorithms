"""DI32 reference: K closest points. Open after your own attempt."""
import heapq

def solve(points, k):
    return heapq.nsmallest(k, points, key=lambda p: (p[0] * p[0] + p[1] * p[1], p[0], p[1]))

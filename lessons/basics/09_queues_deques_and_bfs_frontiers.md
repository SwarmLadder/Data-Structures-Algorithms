# Queues and deques: ordering as an algorithmic tool

**Outcome:** choose FIFO, LIFO or double-ended access based on invariants, and reason about breadth-first exploration. **Study time:** 75–100 minutes.

## 1. Operations and asymptotic guarantees

A stack pops the most recently inserted item; a queue removes the oldest. A Python list supports amortized O(1) append and O(1) pop from the right, making it an effective stack. `pop(0)` shifts the remaining list and is O(n). `collections.deque` supports O(1) append/popleft at the ends and is the right tool for a queue. Random middle-index lookup is not its strong suit.

```python
from collections import deque

def shortest_unweighted(graph, start):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance
```

**BFS invariant:** nodes are removed in nondecreasing distance from start. When neighbor v is first discovered from u, it receives distance d[u]+1. Any shorter path would have discovered v from an earlier layer, contradiction. This proof only applies to unit-weight edges; with nonnegative arbitrary weights choose Dijkstra.

## 2. Trace a small graph

For edges A→B, A→C, B→D, C→D, start queue `[A]`. Pop A and discover B,C (distance 1): queue `[B,C]`. Pop B, discover D (distance 2): queue `[C,D]`. Pop C, see D already visited: unchanged. Pop D: finished. Each vertex enters the queue once, and each edge is inspected once, so O(V+E) time and O(V) queue/visited memory, plus graph storage.

Tie-breaking matters. If shortest paths must be lexicographically smallest, merely using BFS may not be enough unless adjacency iteration order is explicitly sorted and path-selection semantics are justified.

## 3. Sliding-window maximum with a monotone deque

For each new value, remove indices from the **back** whose values are ≤ the incoming value; they can never become maximum while the new value remains in the window. Remove indices from the **front** when they fall outside the current window. The front index then points at the maximum. Every index enters and leaves at most once: O(n) total time despite two while loops.

```python
from collections import deque

def window_max(values, k):
    if not 1 <= k <= len(values):
        return []
    dq, answer = deque(), []
    for i, value in enumerate(values):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and values[dq[-1]] <= value:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            answer.append(values[dq[0]])
    return answer
```

## 4. Why indices instead of values?

Window expiry depends on *where* a value occurred. Two identical values have distinct positions. Store indices to distinguish them. Test `values=[4,4,1,5]`, `k=2`: maxima `[4,4,5]`; tie handling (`<=` versus `<`) determines whether you retain old equals, but both variants can work if expiry is handled correctly.

## Drills

- Rewrite BFS using a list and prove why `pop(0)` may degrade performance.
- Show that a FIFO queue never explores a path with more edges before all shorter paths.
- Implement a circular queue using a fixed-size array and two indexes; state full/empty conditions.
- Trace the deque for `[1,3,-1,-3,5,3,6,7]`, k=3. **Check:** `[3,3,5,5,6,7]`.

**Mastery checkpoint:** Explain why a node enters a queue once, why monotone candidates can be discarded forever, and how deque operations amortize to linear work.

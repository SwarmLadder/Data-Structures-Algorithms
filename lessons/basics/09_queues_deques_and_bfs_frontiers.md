# Queues and deques: ordering as an algorithmic tool

**Outcome:** choose FIFO, LIFO or double-ended access based on invariants, and reason about breadth-first exploration. **Study time:** 75–100 minutes.

**Before this:** [Linked lists: pointer mutation, dummy heads and cycle proofs](08_linked_lists_and_pointer_mutation.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
from collections import deque

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

def bfs_order(graph, start):
    seen, order, queue = {start}, [], deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if nxt not in seen:          # mark when discovered, not when processed
                seen.add(nxt)
                queue.append(nxt)
    return order

print(bfs_order(graph, "A"))

def sliding_max(values, k):
    dq, out = deque(), []
    for i, v in enumerate(values):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and values[dq[-1]] <= v:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(values[dq[0]])
    return out

print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
```

<!-- output -->
```text
['A', 'B', 'C', 'D']
[3, 3, 5, 5, 6, 7]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `list.pop(0)` as a queue | O(n) per dequeue, O(n²) BFS | `collections.deque.popleft()` |
| Marking nodes visited when dequeued | The same node is queued many times | Mark when first discovered |
| Storing values in the window deque | Can't tell when a value expires | Store indexes |
| Assuming BFS gives shortest paths with weights | Wrong distances | BFS is for unit weights; use Dijkstra otherwise |
| Forgetting unreachable nodes | KeyError or missing entries | Decide what unreachable means in the output |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB33` | **Hot potato.** Players stand in a circle in the order given. Repeatedly pass the potato k times (move the front player to the back k times), then remove the player holding it (the new front). Return the order in which players are removed. | guided |
| `DB34` | **Distances from a start node.** graph maps each node (a string) to a list of neighbours. Return a dict of the BFS distance (number of edges) from start to every reachable node. | guided |
| `DB35` | **Sliding-window maximum.** Return the maximum of every contiguous window of size k in values (1 <= k <= len(values)), in O(n) using a deque of indexes. | independent |
| `DB36` | **Recent calls counter.** times is a strictly increasing list of request times in milliseconds. For each request, return how many requests (including itself) happened in the inclusive window [t - 3000, t]. | independent |

```bash
python -m tools.drills show DB33
python -m tools.drills check DB33
python -m tools.drills hint DB33 1
```
<!-- /drills -->

**Interview problems for this lesson:** `A02`, `I14`. Read one with `python -m tools.practice show A02 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why use `deque.popleft()` instead of `list.pop(0)` for a queue?

   - **a)** pop(0) shifts every element: O(n)
   - **b)** deque is sorted
   - **c)** Lists can't pop

**2.** BFS gives shortest paths when…

   - **a)** edges have arbitrary weights
   - **b)** every edge has the same weight
   - **c)** the graph is a tree only

**3.** When should BFS mark a node as seen?

   - **a)** When it is first discovered
   - **b)** When it is dequeued
   - **c)** At the end

**4.** Why does the window-maximum deque hold indexes?

   - **a)** Indexes say when an element expires and distinguish equal values
   - **b)** Smaller memory
   - **c)** deque requires integers

```bash
python -m tools.quiz basics/09 1 b      # question 1, answer b
python -m tools.quiz basics/09           # list the questions
```
<!-- /quiz -->

## Summary

- A queue processes the oldest item first; a deque supports O(1) at both ends.
- BFS explores in layers, so the first discovery of a node gives its shortest unit-weight distance.
- Mark nodes when discovered to queue each at most once.
- A monotone deque of indexes gives sliding-window maxima in O(n).

**Next:** [Sorting: algorithm choice, stability and proof by invariants](10_sorting_stability_and_correctness.md)

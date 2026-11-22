# Worked example A5 · Islands that appear one cell at a time

**Problem.** An empty `rows × cols` sea receives land cells one by one. After each addition, report the number of islands (4-directionally connected land). Re-running a flood fill after every addition is O(k · rows · cols); union–find does it online.

## 1. Plan

Each new cell starts as its own island (count + 1). For each neighbouring land cell, **union** them; every successful union merges two islands (count − 1). Adding the same cell twice changes nothing.

## 2. Tempting attempt: recount with BFS each time

```python
from collections import deque

def islands_recount(rows, cols, positions):
    land, out = set(), []
    for p in positions:
        land.add(tuple(p))
        seen, count = set(), 0
        for cell in land:
            if cell in seen:
                continue
            count += 1
            queue = deque([cell]); seen.add(cell)
            while queue:
                r, c = queue.popleft()
                for nb in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if nb in land and nb not in seen:
                        seen.add(nb); queue.append(nb)
        out.append(count)
    return out

steps = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]]
print(islands_recount(3, 3, steps))
```

<!-- output -->
```text
[1, 1, 2, 3, 1]
```
<!-- /output -->

Correct, which makes it a perfect oracle, but each step costs O(land cells).

## 3. Fix: union–find

```python
def islands(rows, cols, positions):
    parent, out, count = {}, [], 0
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for r, c in positions:
        if (r, c) not in parent:
            parent[(r, c)] = (r, c)
            count += 1
            for nb in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if nb in parent:
                    a, b = find((r, c)), find(nb)
                    if a != b:
                        parent[b] = a
                        count -= 1
        out.append(count)
    return out

print(islands(3, 3, steps))
```

<!-- output -->
```text
[1, 1, 2, 3, 1]
```
<!-- /output -->

The final cell `(1, 1)` touches three islands and merges them into one: three successful unions, count − 3 + 1.

## 4. Test against the recount oracle

```python
import random
random.seed(25)
for _ in range(800):
    rows, cols = random.randint(1, 4), random.randint(1, 4)
    positions = [[random.randrange(rows), random.randrange(cols)] for _ in range(random.randint(0, 10))]
    assert islands(rows, cols, positions) == islands_recount(rows, cols, positions), positions
print("800 random sequences: union-find matches the BFS recount")
```

<!-- output -->
```text
800 random sequences: union-find matches the BFS recount
```
<!-- /output -->

**Practise next:** drills `DA05`, `DA37`; interview problems `A01`, `A05`.

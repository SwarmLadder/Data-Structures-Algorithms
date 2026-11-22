# Worked example A1 · Word ladder: BFS on an implicit graph

**Problem.** Transform `begin` into `end` one letter at a time; every intermediate word must be in `words`. Return the number of words in the shortest ladder (including both ends), or 0.

## 1. Plan

The graph is never given: vertices are words, edges connect words that differ in one letter. Unit-cost edges mean **BFS**. Generate neighbours by pattern (`h*t` matches `hot`, `hit`, `hat`) so we don't compare every pair of words.

## 2. Tempting attempt: DFS

```python
def ladder_dfs(begin, end, words):
    words = set(words)
    best = 0
    def dfs(word, length, seen):
        nonlocal best
        if word == end:
            best = length if not best else min(best, length)
            return
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in words and nxt not in seen:
                    dfs(nxt, length + 1, seen | {nxt})
    dfs(begin, 1, {begin})
    return best

print(ladder_dfs("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
```

<!-- output -->
```text
5
```
<!-- /output -->

It finds the right answer here, but only by trying **every** simple path, which takes exponential time. BFS reaches the end along a shortest path the first time it sees it.

## 3. Fix: BFS with pattern buckets

```python
from collections import defaultdict, deque

def ladder(begin, end, words):
    words = set(words) | {begin}
    if end not in words:
        return 0
    buckets = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            buckets[w[:i] + "*" + w[i + 1:]].append(w)
    dist = {begin: 1}
    queue = deque([begin])
    while queue:
        w = queue.popleft()
        if w == end:
            return dist[w]
        for i in range(len(w)):
            for nxt in buckets[w[:i] + "*" + w[i + 1:]]:
                if nxt not in dist:
                    dist[nxt] = dist[w] + 1
                    queue.append(nxt)
    return 0

print(ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
```

<!-- output -->
```text
5
0
```
<!-- /output -->

Cost: O(N · L) bucket entries for N words of length L, each processed once: **O(N · L²)** including building the pattern strings.

## 4. Test against the exhaustive DFS on small inputs

```python
import random, itertools
random.seed(21)
alphabet = "abc"
all_words = ["".join(p) for p in itertools.product(alphabet, repeat=3)]
for _ in range(300):
    words = random.sample(all_words, random.randint(1, 10))
    begin, end = random.choice(all_words), random.choice(words)
    assert ladder(begin, end, words) == ladder_dfs(begin, end, words), (begin, end, words)
print("300 random dictionaries: BFS matches exhaustive DFS")
```

<!-- output -->
```text
300 random dictionaries: BFS matches exhaustive DFS
```
<!-- /output -->

**Practise next:** drills `DA03`; interview problem `A02`.

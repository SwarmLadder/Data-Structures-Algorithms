# Greedy algorithms: prove the local choice is globally safe

**Outcome:** distinguish a justified greedy rule from a plausible but incorrect heuristic. **Time:** 90–120 minutes.

## 1. Greedy is a theorem, not a data structure

A greedy algorithm repeatedly makes a locally preferred choice and never revisits it. Correctness requires showing that there is always an optimal solution consistent with the choice. Two common proof methods are **exchange arguments** and **staying-ahead arguments**. Neither 'always pick the smallest' nor 'always pick the largest' is valid without a structural reason.

## 2. Select maximum compatible intervals

Given half-open meetings `[start,end)`, select the maximum number of pairwise nonoverlapping meetings. Sort by **earliest finish time**, then accept a meeting when its start ≥ the finish of the last accepted one.

```python
def max_nonoverlapping(meetings):
    chosen = []
    finish = float('-inf')
    for start, end in sorted(meetings, key=lambda p: (p[1], p[0])):
        if start >= finish:
            chosen.append((start, end))
            finish = end
    return chosen
```

**Exchange argument:** Let G be the interval with earliest finish. In an optimal schedule O, let F be its first interval. G ends no later than F, so replacing F with G cannot make any subsequent interval in O start too early. The replacement preserves schedule size, so an optimal schedule beginning with G exists. Apply the same argument to the remaining compatible intervals. Runtime O(n log n) sorting, O(n) output.

## 3. Why a tempting heuristic fails

Choosing shortest duration first is not generally optimal for maximum compatible intervals. Example: `[1,4),[4,7),[3,5)`. The shortest `[3,5)` blocks both others, yielding one; earliest-finish selection can take two. Picking earliest start can likewise choose one long interval that blocks many short ones.

Greedy can also fail for coin change: with denominations `[1,3,4]` and target 6, taking the largest first yields 4+1+1 (three coins), but 3+3 uses two. Use dynamic programming unless denomination structure guarantees greedy optimality.

## 4. When sorting plus greedy works

- **Interval selection:** earliest finish maximizes number selected.
- **Minimum rooms:** earliest start plus heap of end times counts simultaneous usage; it does not itself select a nonoverlapping subset.
- **Huffman coding:** repeatedly merging lowest-frequency trees is optimal given its model, but the proof is not the same as interval scheduling.
- **Kruskal MST:** accept the cheapest edge that connects distinct components; the cut property justifies the choice.

The common principle is an **exchange or safe-edge proof**, not superficial similarity.

## 5. Drill: find a counterexample

If you suspect a greedy rule works, enumerate all tiny instances (e.g., at most six intervals), compare the greedy result with brute force, and search for a mismatch. Counterexample generation is a scientific method for disproving greedy claims. If none is found, that is evidence, not a proof.

## Practice

1. Hand-trace earliest-finish scheduling on `[0,7),[1,3),[3,5),[5,8)`; **check:** three short meetings.
2. Construct an input disproving earliest-start greedy.
3. Explain why changing interval endpoints to *closed* changes the compatibility test.
4. Use exhaustive enumeration to validate greedy scheduling for tiny instances.
5. Compare greedy partition feasibility in lesson 06 with an optimization solved by DP.

**Exit criterion:** Your explanation includes a specific local choice, an exchange/staying-ahead proof, and a concrete counterexample to a tempting incorrect rule.

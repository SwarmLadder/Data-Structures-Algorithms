# Greedy algorithms: prove the local choice is globally safe

**Outcome:** distinguish a justified greedy rule from a plausible but incorrect heuristic. **Time:** 90–120 minutes.

**Study time:** 90–120 minutes · **Before this:** [Heaps: selecting priorities without sorting everything](08_heaps_selection_and_top_k.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def max_non_overlapping(intervals):
    count, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):   # earliest finish first
        if start >= last_end:
            count, last_end = count + 1, end
    return count

jobs = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
print(max_non_overlapping(jobs))

def greedy_coins(amount, coins):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            amount -= c
            used.append(c)
    return used if amount == 0 else None

print(greedy_coins(30, [1, 10, 25]))   # 6 coins, but 3 × 10 is optimal
```

<!-- output -->
```text
3
[25, 1, 1, 1, 1, 1]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Trusting a greedy rule without proof | Plausible but non-optimal answers | Try an exchange argument or find a counterexample |
| Sorting intervals by start for maximum non-overlapping | Long early intervals block many short ones | Sort by end time |
| Greedy coin change for arbitrary coins | Too many coins ([1, 10, 25], amount 30) | Dynamic programming |
| Ignoring ties in the sort key | Different (still valid?) answers | Specify tie-breaking |
| Checking only examples where greedy happens to work | False confidence | Search small inputs exhaustively for a counterexample |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI33` | **Most non-overlapping meetings.** Return the maximum number of pairwise non-overlapping half-open intervals [start, end) you can choose. | guided |
| `DI34` | **Assign cookies.** Child i is content with a cookie of size >= greed[i]. Each child gets at most one cookie. Return the maximum number of content children. | guided |
| `DI35` | **Jump game.** nums[i] is the maximum jump length from index i. Return True if you can reach the last index starting from index 0 (an empty list counts as False). | independent |
| `DI36` | **Does greedy coin change fail?.** Return the smallest amount between 1 and limit for which taking the largest coin first uses more coins than the optimum, or -1 if greedy is optimal for every amount up to limit. coins always contains 1. | independent |

```bash
python -m tools.drills show DI33
python -m tools.drills check DI33
python -m tools.drills hint DI33 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I05`, `I07`. Read one with `python -m tools.practice show I05 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Greedy is a theorem, not a data structure. What does that mean?

   - **a)** A greedy rule needs a proof that the local choice is safe
   - **b)** Greedy always works
   - **c)** Greedy uses no memory

**2.** For maximum non-overlapping intervals, sort by…

   - **a)** start time
   - **b)** end time
   - **c)** length

**3.** Greedy coins [1, 10, 25] for 30 gives 6 coins. The optimum is…

   - **a)** 6
   - **b)** 3
   - **c)** 2

**4.** How does an exchange argument work?

   - **a)** Show any optimal solution can be changed to include the greedy choice without getting worse
   - **b)** Try all permutations
   - **c)** Sort twice

```bash
python -m tools.quiz intermediate/09 1 b      # question 1, answer b
python -m tools.quiz intermediate/09           # list the questions
```
<!-- /quiz -->

## Summary

- A greedy algorithm commits to a locally best choice and never revisits it.
- It's correct only with a proof, usually an exchange argument.
- Earliest-finish-first maximises non-overlapping intervals.
- When greedy fails, a small brute-force search finds the counterexample; switch to DP.

**Next:** [Tries and string algorithms: how to index prefixes](10_tries_strings_and_search_indexes.md)

# Learn to solve unseen problems: contracts, proofs and adversarial testing

**Outcome:** turn a vague algorithm problem into a tested solution without relying on memorized reference code. **Study time:** 90–120 minutes.

**Before this:** [Bits, arithmetic invariants and numerical edge cases](11_bits_integer_arithmetic_and_overflow.md)

## 1. Restate the contract first

Before typing, identify input structure, size limits, output ordering, in-place mutation rules, duplicate/tie semantics, and what happens when no solution exists. For a 'pair sum' question, 'return *any* pair' is fundamentally different from 'return the earliest lexicographic pair' and changes the proof and possibly the algorithm.

Ask what the maximum n rules out: an O(n²) method on n=100,000 can perform ~5×10⁹ comparisons, which is usually impractical. On n=30, O(n²) or even O(2^n) with pruning may be acceptable depending on constants and limits.

## 2. Establish a brute-force oracle

A slow but obvious solution is valuable for verifying a faster one on small inputs:

```python
def brute_max_subarray(nums):
    return max(sum(nums[i:j]) for i in range(len(nums))
               for j in range(i + 1, len(nums) + 1))

def kadane(nums):
    running = best = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best
```

Kadane's invariant: `running` is the maximum sum of a nonempty subarray **ending at the current index**; either start anew with current value or extend the previous best ending. `best` is the best across all processed endpoints. Compare both on random arrays of length up to 12 where brute force is cheap.

## 3. Classify bugs by cause

- **Contract bug:** returns an unordered pair when order is required.
- **Boundary bug:** empty input, single element, off-by-one.
- **Invariant bug:** a window is shrunk before the output candidate is evaluated.
- **Data structure bug:** using list membership inside a loop that needs O(n).
- **Representation bug:** treating bytes as characters or a graph as undirected.
- **Mutability bug:** accidentally modifies an input the caller will reuse.
- **Numerical bug:** fixed-width overflow, floating-point precision or sentinel collision.

For each failed test, save the **smallest counterexample**. A result that is correct on examples but wrong on `[3,3]` often reveals use of the same index twice.

## 4. Randomized differential testing

```python
import random
rng = random.Random(142)
for _ in range(200):
    nums = [rng.randint(-5, 5) for _ in range(rng.randint(1, 10))]
    assert kadane(nums) == brute_max_subarray(nums), nums
```

Fix the seed so failures are reproducible. This is not proof: random testing may miss rare structural cases. Combine it with an invariant proof, edge cases, and **metamorphic tests**. Examples: reversing a linked list twice recovers the original sequence; shuffling an input multiset does not change its frequency counts.

## 5. Use the four-stage interview protocol

1. **Clarify (2 min):** restate contract and constraints, produce an example.
2. **Baseline (3 min):** explain a simple correct approach and its bottleneck.
3. **Optimize (5 min):** choose data structure, state invariant, prove or justify complexity.
4. **Implement/test (15–30 min):** manually trace, test adversarial cases, then articulate tradeoffs.

After reading a solution, close it and reimplement from the invariant after 24 hours, three days, and a week. Recognizing a code snippet is not the same as solving a new problem.

## Drills

- Create three small counterexamples for a broken two-pointer algorithm on arrays with negatives.
- Derive the O(n) Kadane invariant, then compare 200 random tiny arrays with brute force.
- Design edge classes for B01: duplicates, negative complements, zero, first index zero, near-limit n.
- Write a two-minute explanation of why O(n log n) sorting may be acceptable for 100,000 items but O(n²) usually is not.

**Mastery checkpoint:** On an unfamiliar problem, you can obtain a correct baseline, produce an invariant, justify complexity and discover a counterexample without opening the reference code.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
import random

def oracle_max_subarray(nums):
    return max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))

def kadane_fast(nums):
    running = best = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best

random.seed(7)
for trial in range(300):                      # randomized differential test
    nums = [random.randint(-5, 5) for _ in range(random.randint(1, 8))]
    assert kadane_fast(nums) == oracle_max_subarray(nums), nums
print("300 random cases agree")

def buggy_kadane(nums):                        # a tempting bug: best starts at 0
    running = best = 0
    for value in nums:
        running = max(value, running + value)
        best = max(best, running)
    return best

for nums in ([-3], [-2, -1]):
    print(nums, kadane_fast(nums), buggy_kadane(nums))
```

<!-- output -->
```text
300 random cases agree
[-3] -3 0
[-2, -1] -1 0
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Coding before restating the contract | Correct algorithm, wrong output format | Write inputs, outputs, ties and empty cases first |
| No brute-force oracle | Fast solution never checked against truth | Write the slow obvious version for small inputs |
| Random tests with tiny value ranges only | Misses big or negative values | Mix ranges, sizes and duplicates |
| Trusting passing examples | Edge cases fail later | Test empty, single, all-equal, all-negative, max size |
| Debugging by staring | Slow progress | Print the invariant at each step on a failing case |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB45` | **Brute-force oracle: count equal pairs.** Return how many index pairs i < j have nums[i] == nums[j], by checking every pair (this is the oracle; clarity beats speed). | guided |
| `DB46` | **Fast version of the same count.** Same contract as the oracle: count pairs i < j with nums[i] == nums[j], but in O(n) expected time. | guided |
| `DB47` | **Maximum subarray sum (all-negative safe).** Return the largest sum of a non-empty contiguous subarray of nums (len(nums) >= 1). All-negative input must return its largest element. | independent |
| `DB48` | **Which inputs break it?.** buggy(nums) returns max(nums) - min(nums) but crashes on empty input. Return the list of indexes into inputs for which calling max(x) - min(x) would raise (i.e. the empty lists). | independent |

```bash
python -m tools.drills show DB45
python -m tools.drills check DB45
python -m tools.drills hint DB45 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B07`, `B16`. Read one with `python -m tools.practice show B07 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** What is a brute-force oracle for?

   - **a)** Production use
   - **b)** Checking a faster solution on small inputs
   - **c)** Measuring speed

**2.** Kadane initialised with best = 0 fails on…

   - **a)** [1, 2]
   - **b)** [-3]
   - **c)** [0]

**3.** A solution returns the right pair in the wrong order. That's a…

   - **a)** contract bug
   - **b)** complexity bug
   - **c)** boundary bug

**4.** Random differential testing compares…

   - **a)** two runs of the same function
   - **b)** the fast solution with an independent oracle on many random inputs
   - **c)** timing

```bash
python -m tools.quiz basics/12 1 b      # question 1, answer b
python -m tools.quiz basics/12           # list the questions
```
<!-- /quiz -->

## Summary

- Restate the contract: inputs, output order, ties, empty cases, mutation rules.
- A brute-force oracle plus random small inputs finds bugs quickly.
- Classify bugs: contract, invariant, boundary, complexity.
- Explain the invariant, test adversarial inputs, then optimise.

**Next level:** [Intermediate · Sliding windows: maintain a valid contiguous region](../intermediate/01_sliding_windows.md)

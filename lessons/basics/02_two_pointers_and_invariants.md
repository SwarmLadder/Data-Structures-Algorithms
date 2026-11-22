# Two pointers and array invariants

**Outcome:** turn a pair of sorted inputs into one linear pass and reason about what each pointer means.

**Study time:** 75–100 minutes · **Before this:** [Hash maps: find information without repeated scans](01_hashing_and_frequency.md)

Two pointers are valuable when input order provides information. Imagine merging two sorted audit streams. At positions `i` and `j`, the smaller next value must come before every other remaining value in the opposite stream. You can therefore append it and advance only its pointer. Each element advances once, giving **O(n+m)** time instead of sorting all values again.

```python
def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]
```

The **loop invariant** is precise: `out` is sorted and contains exactly the elements already consumed by the pointers. When one array ends, every element still left in the other array may be appended as is. This also explains why duplicate values should not be removed unless the specification explicitly requests a set.

## How to choose the direction

Sometimes pointers begin at opposite ends. In a sorted list containing negative values, the largest square could come from either the most negative element or the most positive element. Compare *absolute values* at the ends and fill the output from right to left. The destination position moves backward as the largest remaining square is selected.

For an alphanumeric palindrome, two pointers also begin at opposite ends, but the invariant is different: all characters outside the window have already been matched, while punctuation can be skipped. The same implementation pattern solves a different proof obligation.

## Interview checks

Ask whether the algorithm changes input arrays. If modification is forbidden, create a separate output. Check one empty array, all duplicates, negative values, and a case where one pointer advances many times before the other moves. State the output-space cost honestly: an O(1)-auxiliary-space algorithm may still need O(n) space to return its answer.

**Practice:** B06, B12, B13, B14. For B12, defend why the next square belongs at the *end* of the result before you write the code. Being able to state this reasoning is the transferable skill.

## Deep dive: the geometry of pointer movement

Two-pointer algorithms are correct only if moving a pointer eliminates candidates that cannot be better. Suppose sorted values at i and j sum to less than target. Moving j left would make the sum no larger, so it cannot repair a too-small sum; move i right. For a sum greater than target, moving i right can only increase it, so move j left. This argument depends on **sorted order**. On unsorted data it is invalid.

### A pointer potential function

Define remaining search width as `j-i+1`. Every iteration reduces the width, so there are at most n iterations even though the algorithm might contain a `while` with conditionals. A separate merge of two arrays has potential `len(a)+len(b)-i-j`, which also decreases on each iteration. State a **decreasing measure** to establish both progress and complexity.

### Stable compaction is a different invariant

Moving zero values uses `read` and `write` pointers traveling in the *same direction*. The prefix `nums[:write]` is the stable sequence of nonzeros seen so far; `read` selects the next element to consider. `write <= read` makes overwriting safe. Unlike the pair-sum search, neither pointer chooses between sorted values; this is an output-construction invariant.

### Counterexamples to wrong assumptions

- Sorted squares: `[-7,-2,3]` becomes `[49,4,9]` if you square in input order. Compare absolute values at both ends, fill the output backward.
- Duplicates: intersection of sorted inventories may preserve multiplicity; `set(a) & set(b)` would lose repeated stock units.
- Input mutation: sorting the data to enable two pointers breaks contracts requiring original indices and unchanged input.
- Empty input: `right=len(nums)-1` yields −1; any access before checking emptiness is a bug.

**Practice:** Implement B06, B12, B13 and B14; draw pointer positions after each step on a small example and state an invariant in plain English. Then prove a maximum of O(n+m) pointer advances and explain all allocated output memory.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def pair_in_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1          # nums[left] can't pair with anything to reach target
        else:
            right -= 1         # nums[right] is too large for every remaining partner
    return []

print(pair_in_sorted([1, 3, 4, 6, 9], 10))
print(pair_in_sorted([1, 2], 7))

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True

print([is_palindrome(w) for w in ["racecar", "ab", "", "a"]])
```

<!-- output -->
```text
[0, 4]
[]
[True, False, True, True]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Using two pointers on unsorted input for pair sums | Discards pairs that exist | Sort first (losing original indexes) or use a hash map |
| `while left <= right` when two different elements are required | An element pairs with itself | `while left < right` |
| Moving both pointers after a mismatch | Skips candidate pairs | Move only the pointer whose element is proven useless |
| Forgetting that sorting destroys original indexes | Wrong indexes returned | Sort (value, index) pairs |
| No proof for why a pointer moves | Correct on examples, wrong on edge cases | State which candidates the move eliminates |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB05` | **Reverse a list in place.** Reverse the list nums in place with two pointers (no slicing or reversed()) and return it. | guided |
| `DB06` | **Pair with a target in a sorted list.** nums is sorted ascending. Return [i, j] (i < j) with nums[i] + nums[j] == target using two pointers, or [] if none exists. If several pairs exist, return the one found by moving the smaller-sum side first (start from both ends). | guided |
| `DB07` | **Remove duplicates from a sorted list.** nums is sorted ascending. Compact it in place so each value appears once, keeping order, and return the number of unique values k. (The checker reads only the return value.) | independent |
| `DB08` | **Is it a palindrome (letters and digits only)?.** Return True if s reads the same forwards and backwards when you ignore every character that isn't a letter or digit and ignore letter case. | independent |

```bash
python -m tools.drills show DB05
python -m tools.drills check DB05
python -m tools.drills hint DB05 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B06`, `B12`, `B13`, `B14`. Read one with `python -m tools.practice show B06 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why can the left pointer move right when the sum is too small (sorted input)?

   - **a)** nums[left] plus any remaining right value is at most the current sum, so it can't reach target
   - **b)** Because left is always smaller
   - **c)** It's a heuristic

**2.** Two pointers on an unsorted list for pair sum…

   - **a)** works the same
   - **b)** can miss valid pairs
   - **c)** is faster

**3.** Time of an opposite-end two-pointer scan?

   - **a)** O(n log n)
   - **b)** O(n²)
   - **c)** O(n)

**4.** Stable compaction with read/write pointers keeps…

   - **a)** the relative order of kept elements
   - **b)** the original indexes
   - **c)** a sorted order

```bash
python -m tools.quiz basics/02 1 b      # question 1, answer b
python -m tools.quiz basics/02           # list the questions
```
<!-- /quiz -->

## Summary

- Two pointers work when each move provably discards candidates that can't be in any answer.
- Opposite-end pointers need sorted (or otherwise monotone) input.
- Same-direction read/write pointers compact or filter arrays in place.
- The number of pointer moves bounds the running time: usually O(n).

**Next:** [Stacks: last-opened, first-closed](03_stacks_and_state.md)

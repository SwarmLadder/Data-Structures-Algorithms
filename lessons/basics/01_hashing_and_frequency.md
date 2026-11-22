# Hash maps: find information without repeated scans

**Outcome:** recognize when a fast lookup beats nested loops, and distinguish a set from a map of counts or indexes.

**Study time:** 75–100 minutes · **Before this:** nothing: this is the first lesson

Suppose an API receives a batch of transaction amounts and you need two values that add up to a threshold. Checking every pair uses two loops and costs **O(n²)** time. A dictionary lets you remember amounts already visited. For the current amount `x`, ask whether `target - x` was seen earlier. This converts repeated searches into average **O(1)** hash lookups, so the full algorithm costs **O(n)** time and **O(n)** space.

```python
def pair_indices(values, target):
    previous = {}
    for right, value in enumerate(values):
        left = previous.get(target - value)
        if left is not None:  # index zero is a valid answer
            return [left, right]
        previous[value] = right
    return []
```

The **invariant** is that the dictionary contains only positions strictly before the current one. It prevents using the same element twice. Notice why `if left:` is incorrect: index `0` is falsy in Python.

A similar tool solves frequency problems, but the stored information changes. `set(items)` answers *has this appeared?*; `Counter(items)` answers *how often?*; a dictionary from value to index answers *where did it appear?* Choose the minimal useful record.

## Deterministic output matters

For grouping anagrams, words such as `"rate"` and `"tear"` share a sorted-letter key. The groups themselves can emerge in insertion order or hash iteration order; that may not satisfy an interviewer who requests sorted output. Always restate the contract: preserve duplicates, sort each group, and sort groups by their first member. A correct grouping with nondeterministic order can still be a wrong answer.

## Failure modes to test

- Duplicates: `[3, 3]` can be a valid pair, but it needs two different indexes.
- Negatives: complements may be positive or negative.
- Missing and empty input: confirm whether the problem guarantees an answer.
- Case sensitivity: `A` and `a` are distinct unless the statement says otherwise.
- Stable tie-breaking: top-frequency elements should resolve alphabetically if specified.

**Practice:** B01, B02, B03, B09, B11. After solving, explain the map's key, value, memory usage, and the exact invariant. Aim for one confident explanation per problem, not just working code.

## Deep dive: collisions, ties, and what the map represents

A hash map is not one universal trick. Start by identifying the **question the map must answer**: `x -> earliest index`, `x -> frequency`, `canonical signature -> group`, or `prefix total -> number of occurrences`. Storing only a set when a count or earliest position is required loses information that cannot be reconstructed in O(1).

### Derive the pair-sum invariant

At loop index j, the dictionary contains **only indices less than j**. For `nums=[3,3]`, `target=6`, querying the complement before inserting current value finds index 0 when j=1. If you insert first, you risk pairing an element with itself. For `nums=[0,4,3,0]`, target 0, a check `if seen.get(complement)` incorrectly rejects index zero because `0` is falsy. Prefer `is not None` or membership checking.

Prove correctness: any valid pair i<j is discovered no later than j, because nums[i] has already been stored when processing j. With a guaranteed unique solution, overwriting an earlier duplicate value does not invalidate the existence of a complement, but if **lexicographically smallest** pairs are required, the overwrite behavior and scan order need reconsideration.

### Cost model beyond O(1)

For fixed-size integer keys, hash-map operations are expected O(1), yielding expected O(n) time and O(n) distinct stored keys. For strings, computing a hash may scan the string's characters and cost O(length). Grouping anagrams by sorting each word of length k takes O(n·k log k), *plus* sorting groups and their elements if deterministic output is required. With a fixed alphabet, a 26-count tuple can sometimes avoid per-word character sorting, trading one key representation for another.

### Construct a revealing test

Consider `['aab','aba','baa','aa']`: the first three must share a group and the fourth must not. Duplicates `['ab','ab']` must remain twice in output if the contract says preserve duplicates. A failed tie test often means you assumed Python's insertion order was the required output order; sort explicitly according to the specification.

**Deliberate practice:** Solve B01, B02, B03, B09 and B11 without using `Counter` once, then compare the custom counts with `Counter`. Explain what value each map stores, which updates happen before queries, and exactly which cases need two maps rather than one.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
from collections import Counter

def find_pair(values, target):
    previous = {}
    for right, value in enumerate(values):
        left = previous.get(target - value)
        if left is not None:
            return [left, right]
        previous[value] = right
    return []

print(find_pair([2, 7, 11, 15], 9))
print(find_pair([3, 3], 6))          # duplicates need two different indexes
print(find_pair([0, 4, 3, 0], 0))    # index 0 is a valid answer

words = ["rate", "tear", "pole", "lope", "tare"]
groups = {}
for word in words:
    groups.setdefault("".join(sorted(word)), []).append(word)
print(sorted(sorted(g) for g in groups.values()))
print(Counter("mississippi").most_common(2))
```

<!-- output -->
```text
[0, 1]
[0, 1]
[0, 3]
[['lope', 'pole'], ['rate', 'tare', 'tear']]
[('i', 4), ('s', 4)]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| `if left:` to test whether a complement was seen | Index 0 is falsy, so a valid pair starting at index 0 is missed | `if left is not None:` or `if key in seen:` |
| Storing the current value before looking up its complement | An element pairs with itself (`[3]`, target 6) | Query first, then insert |
| Using a `set` when the answer needs a position or a count | Information you need was never stored | Choose the record: set / count / first index / list of members |
| Relying on dictionary iteration order for output | Correct groups in an order the contract doesn't allow | Sort explicitly as the contract says |
| Assuming hashing a string is O(1) | Underestimated cost for long keys | Hashing costs O(length) per key |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB01` | **Has a duplicate.** Return True if any value appears at least twice in nums, otherwise False. | guided |
| `DB02` | **Count words.** Return a dict mapping each word of the space-separated string text to how many times it occurs. Words are case-sensitive. | guided |
| `DB03` | **First repeated character.** Return the first character of s that appears for the second time while scanning left to right, or '' if no character repeats. | independent |
| `DB04` | **Most frequent value, smallest on ties.** Return the value that occurs most often in the non-empty list nums. If several values share the highest count, return the smallest of them. | independent |

```bash
python -m tools.drills show DB01
python -m tools.drills check DB01
python -m tools.drills hint DB01 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B01`, `B02`, `B03`, `B09`, `B11`. Read one with `python -m tools.practice show B01 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why is `if seen.get(target - x):` a bug in pair search?

   - **a)** get is slow
   - **b)** Index 0 is falsy, so a valid match at index 0 is ignored
   - **c)** It modifies the dict

**2.** What should the map store to answer "where did this value first appear?"

   - **a)** value -> first index
   - **b)** a set of values
   - **c)** value -> count

**3.** Expected time of the hash-map pair search on n integers?

   - **a)** O(n²)
   - **b)** O(n log n)
   - **c)** O(n)

**4.** Grouping anagrams of n words of length k by sorted letters costs about…

   - **a)** O(n·k log k)
   - **b)** O(n)
   - **c)** O(k)

```bash
python -m tools.quiz basics/01 1 b      # question 1, answer b
python -m tools.quiz basics/01           # list the questions
```
<!-- /quiz -->

## Summary

- A map converts repeated scans into expected O(1) lookups: O(n²) pair search becomes O(n).
- Decide what the map stores: membership, count, first index, or group.
- Invariant for pair search: the map only contains positions strictly before the current one.
- Make output deterministic by sorting according to the contract.

**Next:** [Two pointers and array invariants](02_two_pointers_and_invariants.md)

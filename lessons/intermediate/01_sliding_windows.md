# Sliding windows: maintain a valid contiguous region

**Outcome:** know when a moving window is valid, what must be counted inside it, and why some sums cannot be handled by this pattern.

**Study time:** 90–120 minutes · **Before this:** [Learn to solve unseen problems: contracts, proofs and adversarial testing](../basics/12_debugging_testing_and_reasoning.md)

The sliding-window technique processes a *contiguous* interval while adjusting only its endpoints. In the longest substring with no repeated character, keep a start position and the most recent index of each character. When a character repeats inside the current region, move the start **after** its previous occurrence. Do not move the start backward: an earlier duplicate outside the current region has already been resolved.

```python
def longest_distinct(text):
    last = {}
    left = best = 0
    for right, character in enumerate(text):
        if character in last:
            left = max(left, last[character] + 1)
        last[character] = right
        best = max(best, right - left + 1)
    return best
```

Each index advances forward at most once. The overall time is O(n); memory depends on the distinct characters, not the number of possible substrings.

## Windows with counts

The smallest substring containing a required multiset is more subtle. Membership is not enough: if the requirement is `"AAB"`, one `A` cannot count twice. Maintain a frequency deficit for the requirement and a counter of how many **total required character occurrences** are still missing. Expand the right side until the deficit reaches zero. Shrink the left side until removing another character would break the requirement, updating the best answer along the way.

For *at most k distinct characters*, use a map of window frequencies. Reduce the left side only when the number of distinct keys exceeds `k`. Remove a key when its count reaches zero; leaving zero-count entries will make the distinct-count test incorrect.

## Where the pattern breaks

A common mistake is using a sum-based sliding window when negative numbers are permitted. The window sum no longer changes predictably with its width. For counting target-sum subarrays with negative numbers, use prefix-sum frequencies instead. Choosing the wrong pattern can produce plausible answers for simple positive-only examples and fail interview edge cases.

**Practice:** I01, I02, I04. Draw how the left and right pointers move for `"abba"`, `"ADOBECODEBANC"` with `"ABC"`, and `"eceba"` with k=2. Describe the validity condition, the moment to shrink, and the tie-breaking rule.

## Deep dive: the proof that shrinking is safe

A window has a left and right boundary, but that does not make it a valid sliding-window algorithm. You need a property that permits discarding prefixes irrevocably. For the longest substring without repeated characters, when the same character reappears, every window still containing its earlier occurrence is invalid. Moving left past that occurrence therefore cannot discard a valid candidate ending at the current right index.

### Jumping the boundary in O(n)

Store the last observed index of each character. On seeing character c at `right`, set `left=max(left,last[c]+1)` to keep the boundary monotone. The `max` matters: the last occurrence might be *outside* the current window. For `'abba'`, after the second b we move left to index 2; the final a occurred at index 0 and must not move the window backward.

### Minimum covering window counts multiplicity

If required is `'AABC'`, a window with one A, one B and one C is insufficient. Maintain deficits for each required character. A counter of *missing occurrences*—not just missing distinct keys—allows O(1) updates. Expand right until valid, then shrink left while maintaining validity, recording shortest candidates before removing a required character. At most 2n boundary movements gives O(n) time plus alphabet-memory.

### Why negative values break some windows

For sum-at-most-k with nonnegative numbers, adding on the right cannot decrease a sum, so shrinking the left is justified when the sum exceeds k. With negative values, adding a new element may decrease the sum later; shrinking now might discard a future valid range. For arbitrary signed target-sum counts use prefix sums and frequencies instead.

**Practice:** I01, I02 and I04; explicitly describe what happens for empty requirements, duplicate required characters, k=0 and a repeated character outside the current window. Explain how tie-breaking chooses the earliest minimal window when several have equal length.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
def longest_unique(s):
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1           # jump past the previous copy
        last[ch] = right
        best = max(best, right - left + 1)
    return best

for s in ["abcabcbb", "bbbbb", "pwwkew", ""]:
    print(repr(s), longest_unique(s))

def max_sum_window(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]   # slide: add the new, drop the old
        best = max(best, window)
    return best

print(max_sum_window([2, 1, 5, 1, 3, 2], 3))
```

<!-- output -->
```text
'abcabcbb' 3
'bbbbb' 1
'pwwkew' 3
'' 0
9
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Using a variable window with negative numbers for 'sum ≥ target' | Shrinking is no longer safe; wrong answers | Use prefix sums (+ a deque or sorted structure) |
| Moving `left` backwards on a jump | Window grows past a repeat | `left = max(left, last[ch] + 1)` or check `last[ch] >= left` |
| Recomputing the window sum each step | O(n·k) | Add the entering element, subtract the leaving one |
| Comparing counts with `==` on whole dicts every step | O(alphabet) per step, often fine but hides intent | Track how many requirements are satisfied |
| Off-by-one window length | Answers one too long or short | Length of [left, right] is right − left + 1 |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DI01` | **Maximum sum of k consecutive values.** Return the largest sum of any k consecutive values in nums (1 <= k <= len(nums)), in O(n). | guided |
| `DI02` | **Shortest subarray with sum at least target.** nums contains positive integers. Return the length of the shortest contiguous subarray whose sum is >= target, or 0 if none exists. | guided |
| `DI03` | **Longest run with at most k flips.** bits contains 0s and 1s. Return the length of the longest contiguous run of 1s you can get by flipping at most k zeros. | independent |
| `DI04` | **Is a permutation of p inside s?.** Return True if some contiguous substring of s is a rearrangement of p (same letters, same counts). | independent |

```bash
python -m tools.drills show DI01
python -m tools.drills check DI01
python -m tools.drills hint DI01 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I01`, `I02`, `I04`. Read one with `python -m tools.practice show I01 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Why is shrinking the left edge safe when looking for the longest window without repeats?

   - **a)** Removing characters from a window without repeats can't create a repeat
   - **b)** Windows are always sorted
   - **c)** Because the right edge never moves

**2.** A variable sliding window for 'sum ≥ target' breaks when…

   - **a)** values can be negative
   - **b)** values are large
   - **c)** the target is zero

**3.** Total pointer moves in a variable window over n items?

   - **a)** O(n²)
   - **b)** At most 2n
   - **c)** O(n log n)

**4.** For the minimum covering window, requirements are counted with…

   - **a)** a set of letters
   - **b)** multiplicity: how many of each letter are still needed
   - **c)** a sorted list

```bash
python -m tools.quiz intermediate/01 1 b      # question 1, answer b
python -m tools.quiz intermediate/01           # list the questions
```
<!-- /quiz -->

## Summary

- A window is valid or invalid; grow the right edge and shrink the left only while it stays safe.
- Shrinking is safe when validity is monotone: removing elements can't make an invalid window valid (or the reverse).
- Fixed-size windows slide in O(1) per step; variable windows move each edge at most n times.
- Negative values break many sum-window arguments; switch to prefix sums.

**Next:** [Prefix sums: turn range questions into dictionary lookups](02_prefix_sums_and_counts.md)

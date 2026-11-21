# Sliding windows: maintain a valid contiguous region

**Outcome:** know when a moving window is valid, what must be counted inside it, and why some sums cannot be handled by this pattern.

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

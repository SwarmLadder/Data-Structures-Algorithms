# Arrays and strings: indexes, range invariants, and stable transforms

**Outcome:** analyze contiguous structures, design safe in-place algorithms, and handle boundaries rigorously. **Study time:** 90 minutes.

## 1. Understand the data representation

Python lists are dynamically sized arrays of **references**. Reading or assigning `a[i]` is O(1); append is amortized O(1); inserting at the front usually shifts O(n) references. Python strings are immutable; a loop that repeatedly appends to a string can perform repeated copying. Build a list of fragments and join once.

Prefer **half-open intervals** [lo, hi): length hi−lo, empty when lo=hi, and adjacent ranges compose without overlap. Python slices follow this model. Every time you use inclusive bounds, write down exactly what hi represents to avoid accessing `a[len(a)]`.

## 2. Stable zero compaction

Problem: move zeros to the right while keeping nonzero values in original relative order and without creating a second list.

```python
def move_zeros(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
```

**Loop invariant:** before processing position read, `nums[:write]` contains exactly the nonzero values encountered in `nums[:read]`, in their original order. Also 0 ≤ write ≤ read. If current value is nonzero, copying it to `nums[write]` extends the desired prefix; otherwise the prefix stays valid. Termination: read reaches n; zero-filling the remaining n−write slots yields the required sequence. Time O(n), additional space O(1). A repeated `remove(0)` algorithm can be O(n²) because every removal shifts elements.

Trace `[0,4,0,5,7]`: after read 1, prefix `[4]`; after read 3, `[4,5]`; after read 4, `[4,5,7]`; final array `[4,5,7,0,0]`.

## 3. Prefixes and rotations

For a longest common prefix, inspect characters by column until a string ends or a mismatch occurs:

```python
def common_prefix(words):
    if not words:
        return ''
    for i, symbol in enumerate(words[0]):
        if any(i >= len(word) or word[i] != symbol for word in words[1:]):
            return words[0][:i]
    return words[0]
```

With m strings and candidate length L, worst-case time O(mL) plus O(L) for the returned prefix. Validate empty inputs; do not assume words have equal lengths.

For rotation by k, handle n=0 before calculating `k %= n`; then choose between a concise slicing solution (O(n) allocated output) and the in-place three-reversal trick (O(1) extra memory). The contract decides which approach is appropriate.

## 4. Sorted squares and output-direction reasoning

A sorted array such as `[-8,-3,1,6]` has squares `[64,9,1,36]`, not sorted. The largest **magnitude** is always at one end. Compare the absolute values of left and right pointers, write the larger square into the rightmost available output slot, and move that pointer. Output slots shrink monotonically from right to left. Time O(n), output O(n), versus O(n log n) to sort squared values.

## 5. Strings and Unicode constraints

Specify whether 'character' means code point, byte, or grapheme cluster. Python iterates Unicode code points, which may not correspond to human-perceived characters. Many interview questions explicitly restrict input to ASCII or lowercase a–z; exploit those constraints only when they are stated. A fixed 26-element frequency vector gives O(1) **alphabet-size** space, whereas a hash map supports arbitrary keys.

## Drills

- Trace write/read on `[0,0,1,2,0,3]`. Show the invariant after every nonzero.
- Implement sorted squares by filling from the right; test all-negative and all-positive arrays.
- Rotate `[1,2,3,4,5]` by 7 positions. **Check:** `[4,5,1,2,3]`.
- Test common prefix on `[]`, `['']`, `['prefix','pre','prevent']`, and unrelated strings.
- Compare memory and correctness of in-place versus out-of-place solutions for B08 and B14.

**Practice links:** B06, B08, B12, B14, B15, B16. **Mastery checkpoint:** You can write a loop invariant describing processed and unprocessed slices, prove indices stay in range, and distinguish output size from auxiliary memory.

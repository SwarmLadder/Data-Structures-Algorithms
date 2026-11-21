# Bits, arithmetic invariants and numerical edge cases

**Outcome:** use bit operations and arithmetic safely, especially when interview implementations assume fixed-width integers. **Study time:** 75–100 minutes.

## 1. Bits as compact state

A bitset stores boolean flags in integer bits: set bit k with `mask |= 1 << k`, check with `mask & (1 << k)`, clear with `mask &= ~(1 << k)`. This is useful when a problem has a small finite set of states (e.g., a–z letters or n≤20 chosen elements). An integer mask can encode a subset, but enumerating every mask still takes 2^n time.

```python
def unique_lowercase_letters(text):
    mask = 0
    for ch in text:
        bit = 1 << (ord(ch) - ord('a'))
        if mask & bit:
            return False
        mask |= bit
    return True
```

Only use this if all characters are lowercase a–z. With arbitrary input the shift could become negative or huge. Explicit constraints are part of the algorithm.

## 2. XOR properties and their limits

`x ^ x == 0`, `x ^ 0 == x`, and XOR is associative/commutative. If every integer occurs twice except one, XOR of all items yields the singleton in O(n) time and O(1) extra space. It **does not** solve a problem where one value occurs three times or several values have odd counts without additional assumptions.

```python
def singleton(nums):
    answer = 0
    for x in nums:
        answer ^= x
    return answer
```

Python integers have arbitrary precision rather than fixed 32-bit wraparound. For signed fixed-width complement problems, normalize with a mask `& ((1 << width)-1)` and explain how negative values should be represented.

## 3. Derive missing-value formulas

If the input contains every integer from 0..n except exactly one, the expected sum is n(n+1)/2. Subtract the observed sum to get the missing value. Time O(n), extra space O(1). The formula is invalid when duplicates or out-of-range values exist. In 32-bit languages, n(n+1) may overflow unless promoted to a wider type; Python integer arithmetic avoids that specific overflow but still consumes time/memory for enormous numbers.

## 4. Counting set bits

Kernighan's trick uses `x &= x-1` to clear the lowest set bit of a positive integer. Each iteration removes one set bit, so runtime O(popcount(x)), bounded by bit width. This can be faster than checking every position when the mask is sparse.

```python
def bit_count_positive(x):
    if x < 0:
        raise ValueError('Use a declared fixed width for negative values')
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count
```

## 5. Modular arithmetic

When counting combinations modulo M, apply `% M` after additions/multiplications to bound values. Do not divide ordinary integers modulo M unless an inverse exists (usually requiring coprimality). Binary search midpoint in fixed-width languages is often written `lo + (hi-lo)//2` to avoid overflow; in Python this is a style choice, not an overflow necessity.

## Drills

- Trace masks while processing `abca`. **Check:** duplicate a is detected at the fourth character.
- Evaluate 13 in binary and count its set bits using x&(x−1). **Check:** 3 steps.
- Show a counterexample where the 0..n missing-value formula fails when duplicates are present.
- Compare XOR singleton with a Counter implementation; explain which input contracts allow which.
- Design a bitmask state for a backtracking problem with n≤16 independent tasks.

**Mastery checkpoint:** You can state representation width, signedness, preconditions, overflow constraints and when a bit trick is valid.

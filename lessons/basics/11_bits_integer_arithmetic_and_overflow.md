# Bits, arithmetic invariants and numerical edge cases

**Outcome:** use bit operations and arithmetic safely, especially when interview implementations assume fixed-width integers. **Study time:** 75–100 minutes.

**Before this:** [Sorting: algorithm choice, stability and proof by invariants](10_sorting_stability_and_correctness.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
mask = 0
for bit in (0, 3, 5):
    mask |= 1 << bit
print(bin(mask), bool(mask & (1 << 3)), bool(mask & (1 << 4)))

def xor_singleton(nums):
    answer = 0
    for x in nums:
        answer ^= x
    return answer

print(xor_singleton([4, 1, 2, 1, 2]))

def popcount(x):
    count = 0
    while x:
        x &= x - 1          # clears the lowest set bit
        count += 1
    return count

print(popcount(13), bin(13), (13).bit_count())
print(-1 & 0xFFFFFFFF)          # 32-bit two's-complement view of -1
print((10 ** 20 + 7) % 1_000_000_007)
```

<!-- output -->
```text
0b101001 True False
4
3 0b1101 3
4294967295
4907
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Using bit tricks outside their preconditions | Wrong answers when values repeat 3 times or are negative | State the precondition (e.g. 'every other value appears exactly twice') |
| Assuming 32-bit overflow in Python | Python ints never overflow | Mask with `& 0xFFFFFFFF` when fixed width is required |
| `1 << ord(ch)` on arbitrary characters | Huge integers or negative shifts | Restrict to the declared alphabet |
| `x & 1 == 0` without parentheses | `==` binds tighter: `x & (1 == 0)` | Write `(x & 1) == 0` |
| Dividing under a modulus | Wrong results | Use a modular inverse (when one exists) |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB41` | **The value without a partner.** Every value in nums appears exactly twice except one. Return that value using XOR (O(1) extra space). | guided |
| `DB42` | **Is it a power of two?.** Return True if the integer n is a positive power of two (1, 2, 4, …), using a bit trick. | guided |
| `DB43` | **Count set bits from 0 to n.** Return a list whose i-th entry is the number of 1 bits in i, for every i from 0 to n, in O(n) using the relation bits(i) = bits(i >> 1) + (i & 1). | independent |
| `DB44` | **The missing number.** nums contains n distinct numbers taken from 0..n (so exactly one is missing). Return the missing one in O(n) time and O(1) extra space. | independent |

```bash
python -m tools.drills show DB41
python -m tools.drills check DB41
python -m tools.drills hint DB41 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B10`. Read one with `python -m tools.practice show B10 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** XOR of all values finds the singleton only if…

   - **a)** every other value appears exactly twice (an even number of times)
   - **b)** values are sorted
   - **c)** values are positive

**2.** What does `x & (x - 1)` do?

   - **a)** Doubles x
   - **b)** Clears the lowest set bit
   - **c)** Sets every bit

**3.** Python's `2**31 + 2**31` overflows to a negative number?

   - **a)** Yes
   - **b)** No, Python integers are unbounded
   - **c)** Only on 32-bit machines

**4.** Why does the sum formula fail if the input may contain duplicates?

   - **a)** Sums are slow
   - **b)** Its precondition (all distinct, exactly one missing) no longer holds
   - **c)** It always works

```bash
python -m tools.quiz basics/11 1 b      # question 1, answer b
python -m tools.quiz basics/11           # list the questions
```
<!-- /quiz -->

## Summary

- Bitmasks store small sets of flags: set with `|=`, test with `&`, clear with `&= ~`.
- XOR cancels pairs: the XOR of a list where everything appears twice except one value is that value.
- `x & (x - 1)` clears the lowest set bit; loop it to count bits.
- Python integers are unbounded; simulate fixed width explicitly with masks.

**Next:** [Learn to solve unseen problems: contracts, proofs and adversarial testing](12_debugging_testing_and_reasoning.md)

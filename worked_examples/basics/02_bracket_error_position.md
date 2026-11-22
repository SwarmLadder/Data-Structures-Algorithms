# Worked example B2 · Report where the brackets break

**Problem.** A config validator must say not just *whether* brackets `()[]{}` balance, but **the index of the first error**: the first unmatched closer, or, if every closer matched, the first opener left unclosed. Return `-1` if balanced.

## 1. Plan

A stack of unmatched openers already exists in the yes/no version. Store **indexes** instead of characters, and the error position falls out:

- a closer with an empty stack, or the wrong opener on top → error at the closer;
- leftover openers at the end → error at the **bottom** of the stack (the earliest unclosed one).

## 2. Tempting attempt

```python
PAIR = {")": "(", "]": "[", "}": "{"}

def first_error_wrong(s):
    stack = []
    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append(i)
        elif ch in PAIR:
            if not stack or s[stack.pop()] != PAIR[ch]:
                return i
    return stack[-1] if stack else -1            # reports the LAST unclosed opener

print(first_error_wrong("((x)"), first_error_wrong("(()"))
```

<!-- output -->
```text
0 0
```
<!-- /output -->

Both answers are right only because a single opener is left unclosed, so `stack[-1]` happens to be the earliest one. With several unclosed openers it reports the **last** one: `"(()("` gives 3 instead of 0.

```python
print(first_error_wrong("(()("))
```

<!-- output -->
```text
3
```
<!-- /output -->

## 3. Fix

```python
def first_error(s):
    stack = []
    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append(i)
        elif ch in PAIR:
            if not stack or s[stack.pop()] != PAIR[ch]:
                return i
    return stack[0] if stack else -1             # the earliest unclosed opener

for sample in ["{[()]}", "([)]", "(()(", "]", "", "a{b(c)d"]:
    print(repr(sample), first_error(sample))
```

<!-- output -->
```text
'{[()]}' -1
'([)]' 2
'(()(' 0
']' 0
'' -1
'a{b(c)d' 1
```
<!-- /output -->

## 4. Test it

An oracle for "first unmatched closer" is easy to write differently: repeatedly delete adjacent matching pairs, then the remaining structure tells the answer. Simpler still, test the **yes/no** consequence against an independent checker:

```python
import random

def balanced_by_reduction(s):
    s = "".join(ch for ch in s if ch in "()[]{}")
    while any(p in s for p in ("()", "[]", "{}")):
        for p in ("()", "[]", "{}"):
            s = s.replace(p, "")
    return s == ""

random.seed(2)
for _ in range(3000):
    s = "".join(random.choice("()[]{}x") for _ in range(random.randint(0, 8)))
    assert (first_error(s) == -1) == balanced_by_reduction(s), s
print("3000 random strings: -1 exactly when balanced")
```

<!-- output -->
```text
3000 random strings: -1 exactly when balanced
```
<!-- /output -->

**Practise next:** drills `DB09`, `DB10`; interview problem `B04`.

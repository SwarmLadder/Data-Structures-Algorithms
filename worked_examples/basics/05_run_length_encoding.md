# Worked example B5 · Run-length encoding and its inverse

**Problem.** Compress `"aaabccdddd"` to `"a3b1c2d4"` and decompress it back. Prove the round trip with tests.

## 1. Plan

Scan once, tracking where the current run started. A run ends when the next character differs **or the string ends**. That last condition is the classic place to drop data.

## 2. Tempting attempt

```python
def encode_wrong(s):
    out, start = [], 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            out.append(f"{s[start]}{i - start}")
            start = i
    return "".join(out)

print(encode_wrong("aaabccdddd"))      # the final run "d4" is missing
```

<!-- output -->
```text
a3b1c2
```
<!-- /output -->

The loop only emits a run when it sees the *next* run begin, so the last run is never written.

## 3. Fix

```python
def encode(s):
    out, start = [], 0
    for i in range(1, len(s) + 1):     # i == len(s) acts as a sentinel "end of string"
        if i == len(s) or s[i] != s[i - 1]:
            out.append(f"{s[start]}{i - start}")
            start = i
    return "".join(out) if s else ""

def decode(code):
    out, i = [], 0
    while i < len(code):
        ch, j = code[i], i + 1
        while j < len(code) and code[j].isdigit():
            j += 1                     # counts can have several digits
        out.append(ch * int(code[i + 1:j]))
        i = j
    return "".join(out)

print(encode("aaabccdddd"), decode(encode("aaabccdddd")))
print(repr(encode("")), encode("z"), encode("x" * 12), decode("x12"))
```

<!-- output -->
```text
a3b1c2d4 aaabccdddd
'' z1 x12 xxxxxxxxxxxx
```
<!-- /output -->

**Invariant:** after processing index `i`, `out` encodes exactly `s[:start]`, and `s[start:i]` is one run of `s[start]`.

## 4. Test the round trip

`decode(encode(s)) == s` must hold for every string of letters, which is a perfect property test:

```python
import random
random.seed(5)
for _ in range(3000):
    s = "".join(random.choice("ab") * random.randint(1, 12) for _ in range(random.randint(0, 5)))
    assert decode(encode(s)) == s, s
print("3000 random strings survive the round trip")
```

<!-- output -->
```text
3000 random strings survive the round trip
```
<!-- /output -->

**Practise next:** drills `DB05`, `DB23`; interview problem `B14`.

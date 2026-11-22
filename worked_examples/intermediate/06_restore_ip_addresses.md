# Worked example I6 · Restore IP addresses with sound pruning

**Problem.** Given a string of digits, return every valid IPv4 address you can form by inserting three dots. Each part is 0–255 with no leading zeros (`"0"` is fine, `"01"` isn't). Return addresses in sorted order.

## 1. Plan

Backtracking over 4 parts, each 1–3 digits. Two prunes keep it fast:

- a part is invalid if it has a leading zero or exceeds 255;
- the **remaining digits** must fit: between `parts_left` and `3 × parts_left` characters.

## 2. Tempting attempt: no leading-zero check

```python
def restore_wrong(s):
    out = []
    def dfs(start, parts):
        if len(parts) == 4:
            if start == len(s):
                out.append(".".join(parts))
            return
        for size in (1, 2, 3):
            piece = s[start:start + size]
            if len(piece) == size and int(piece) <= 255:
                dfs(start + size, parts + [piece])
    dfs(0, [])
    return sorted(out)

print(restore_wrong("10023"))
```

<!-- output -->
```text
['1.0.0.23', '1.0.02.3', '1.00.2.3', '10.0.2.3']
```
<!-- /output -->

`"1.0.02.3"` and `"1.00.2.3"` are accepted, but parts with leading zeros (`"02"`, `"00"`) are not valid IPv4 octets.

## 3. Fix with both prunes

```python
def restore(s):
    out = []
    def valid(piece):
        return piece == "0" or (piece[0] != "0" and int(piece) <= 255)
    def dfs(start, parts):
        left = 4 - len(parts)
        remaining = len(s) - start
        if remaining < left or remaining > 3 * left:   # can't possibly fit
            return
        if left == 0:
            out.append(".".join(parts))
            return
        for size in (1, 2, 3):
            piece = s[start:start + size]
            if len(piece) == size and valid(piece):
                dfs(start + size, parts + [piece])
    dfs(0, [])
    return sorted(out)

for s in ["25525511135", "0000", "10023", "1111111111111"]:
    print(s, restore(s))
```

<!-- output -->
```text
25525511135 ['255.255.11.135', '255.255.111.35']
0000 ['0.0.0.0']
10023 ['1.0.0.23', '10.0.2.3']
1111111111111 []
```
<!-- /output -->

## 4. Test against brute force over all dot positions

```python
import itertools, random

def brute(s):
    out = set()
    for a, b, c in itertools.combinations(range(1, len(s)), 3):
        parts = [s[:a], s[a:b], s[b:c], s[c:]]
        if all(p and (p == "0" or (p[0] != "0" and int(p) <= 255)) for p in parts):
            out.add(".".join(parts))
    return sorted(out)

random.seed(16)
for _ in range(1500):
    s = "".join(random.choice("0125") for _ in range(random.randint(0, 12)))
    assert restore(s) == brute(s), s
print("1500 random strings agree with brute force")
```

<!-- output -->
```text
1500 random strings agree with brute force
```
<!-- /output -->

**Practise next:** drills `DI41`, `DI43`; interview problems `A14`, `A15`.

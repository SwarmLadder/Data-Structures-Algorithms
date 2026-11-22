# Stacks: last-opened, first-closed

**Outcome:** understand when a stack captures the order of unfinished work more naturally than recursion or a dictionary.

**Study time:** 75–100 minutes · **Before this:** [Two pointers and array invariants](02_two_pointers_and_invariants.md)

Consider brackets in a configuration expression: `([{}])` is valid, but `([)]` is not. Counting each type of bracket is insufficient. Both strings have the same counts; nesting order is the real constraint. Maintain a stack of unmatched opening brackets. On a closing bracket, demand a matching bracket on top, and remove it. At the end the stack must be empty.

```python
def valid_brackets(text):
    matches = {')': '(', ']': '[', '}': '{'}
    pending = []
    for character in text:
        if character in '([{':
            pending.append(character)
        elif not pending or pending.pop() != matches[character]:
            return False
    return not pending
```

The **invariant** is that `pending` contains the exact sequence of openings that have not been matched, in occurrence order. The most recent must close first: **LIFO**. Each character enters or leaves the stack at most once, so the runtime is **O(n)** and worst-case space is **O(n)**.

## From matching to monotonic stacks

A related technique answers questions like *how many days until a higher latency occurs?* Keep unresolved positions in a stack. Unlike the bracket stack, this one is ordered by values: each new greater value resolves a run of earlier waiting positions. It is called a **monotonic stack**. Elements may be pushed and popped once, so nested-looking loops still have linear total work.

The difference between the two patterns matters. Bracket matching uses nesting; next-greater-element problems exploit a **monotonic relation**. Do not choose a stack simply because the question involves history. Identify what remains unresolved and which future event can resolve it.

## Validate the boundary cases

Test an empty string, one closing bracket, leftover openings, crossing brackets, and deeply nested input. For next-greater values, test equal neighbors: a strictly greater requirement does not allow an equal value to resolve a position. Ask whether the answer should be an index, distance, or value before choosing what to store.

**Practice:** B04 and I09. Describe the meaning of each stack element and explain how many times any element can be pushed or popped.

## Deep dive: stack contents are a compact proof

A stack does not just hold values; it captures the **unresolved work** from the processed prefix. For balanced delimiters, every opening bracket pushed is waiting for a closing bracket; the most recently opened must close first. If a closing bracket mismatches the top of the stack, no future character can repair the nesting already violated. This is why early rejection is safe.

### Trace a nontrivial sequence

For `'{[()]}'`, stacks after each character are `['{']`, `['{','[']`, `['{','[','(']`, `['{','[']`, `['{']`, `[]`. For `'([)]'`, the third symbol is `)` while `[` is on top, so reject immediately. Counting the total number of left/right delimiters cannot detect this violation.

### Monotonic stacks store indices, not just values

For daily latency `[7,4,6,8]`, an unresolved-index stack starts `[0]` for 7, becomes `[0,1]` for 4, then 6 pops index 1 and sets wait 1. Finally 8 pops index 2 and index 0. Every index is pushed once and popped once: O(n) total work, even with a nested while loop. Equal values remain unresolved if the question requires a **strictly** higher next value; changing `<` to `<=` changes semantics.

### Stack versus recursion

An explicit stack is the iterative counterpart to DFS's call stack. For preorder traversal, push a node's right child before its left child so left is visited first. A recursive traversal of a 100,000-node chain may exceed Python's recursion limit; an explicit stack handles depth without Python recursive frames but still uses O(n) memory in the worst case.

**Failure tests:** unmatched opener, unmatched closer, incorrect nesting, empty input, repeated equal latency values, entirely decreasing latency sequence. **Practice:** B04 and I09; for each explain the invariant, the reason popped items will never be relevant again, and the stack's maximum size.

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
PAIRS = {")": "(", "]": "[", "}": "{"}

def balanced(text):
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return not stack

for sample in ["{[()]}", "([)]", "((", "", "a(b)c"]:
    print(repr(sample), balanced(sample))

def next_greater(values):
    answer, stack = [-1] * len(values), []   # stack holds indexes still waiting
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(i)
    return answer

print(next_greater([2, 1, 2, 4, 3]))
```

<!-- output -->
```text
'{[()]}' True
'([)]' False
'((' False
'' True
'a(b)c' True
[4, 2, 4, -1, -1]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Popping from an empty stack on a closing bracket | IndexError on input like `)(` | Check `not stack` first |
| Returning True after the loop without checking the stack | `((` counted as balanced | Return `not stack` |
| Storing values instead of indexes in a monotonic stack | Can't write the answer back to the right position | Push indexes |
| Calling a nested while-loop O(n²) | Overestimated cost | Each index is pushed and popped once: amortized O(n) |
| Recursion for deep nesting | RecursionError around 1000 levels | Use an explicit stack |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB09` | **Only round brackets.** Return True if every '(' in s is closed by a later ')' and no ')' appears without a matching '('. Other characters are ignored. | guided |
| `DB10` | **Undo with backspaces.** In s, the character '#' deletes the previous surviving character (if any). Return the final text. | guided |
| `DB11` | **Evaluate reverse Polish notation.** tokens is a valid expression in reverse Polish notation using integers and the operators + - * /. Division truncates toward zero (like int(a / b)). Return the value. | independent |
| `DB12` | **Days until a warmer day.** For each day i in temps, return how many days you wait until a strictly warmer temperature, or 0 if none comes. | independent |

```bash
python -m tools.drills show DB09
python -m tools.drills check DB09
python -m tools.drills hint DB09 1
```
<!-- /drills -->

**Interview problems for this lesson:** `B04`, `I09`. Read one with `python -m tools.practice show B04 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Which input breaks a checker that returns True after the loop without checking the stack?

   - **a)** "()"
   - **b)** "(("
   - **c)** ")("

**2.** In a next-greater scan, why store indexes instead of values?

   - **a)** Indexes use less memory
   - **b)** The answer must be written to the waiting element's position
   - **c)** Values can't be compared

**3.** Total time of the monotonic-stack next-greater algorithm?

   - **a)** O(n²) because of the inner while
   - **b)** O(n log n)
   - **c)** O(n) amortized

**4.** Why prefer an explicit stack over recursion for deeply nested input in Python?

   - **a)** The recursion limit (about 1000 frames) can be exceeded
   - **b)** Stacks are always faster
   - **c)** Recursion can't express nesting

```bash
python -m tools.quiz basics/03 1 b      # question 1, answer b
python -m tools.quiz basics/03           # list the questions
```
<!-- /quiz -->

## Summary

- A stack holds unfinished work, most recent first: perfect for nesting.
- Balanced brackets: push openers, match closers, and require an empty stack at the end.
- A monotonic stack keeps indexes still waiting for an answer; each is pushed and popped once.
- Explicit stacks replace recursion when depth could be large.

**Next:** [Binary search, prefix computation and one-dimensional DP](04_binary_search_prefixes_and_dp.md)

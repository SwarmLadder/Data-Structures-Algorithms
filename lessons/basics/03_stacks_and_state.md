# Stacks: last opened, first closed

**Outcome:** use a stack whenever the newest unfinished item must be finished first, and recognise when a monotonic stack answers "what comes next?" in linear time.

**Study time:** 45–60 minutes · **Before this:** [Two pointers and array invariants](02_two_pointers_and_invariants.md)

## 1. A stack holds unfinished work

- `append` pushes onto the top and `pop` removes the most recent item: last in, first out (LIFO). Both are O(1).
- `stack[-1]` reads the top without removing it. Check `if stack` first: popping an empty list raises `IndexError`.
- Reach for a stack when the newest unfinished thing must be finished first: brackets, undo, nested calls.

```python
stack = []
for action in ["open file", "type title", "type body"]:
    stack.append(action)
    print("push", repr(action), "->", stack)
print("undo", repr(stack.pop()), "->", stack)
print("top is now", repr(stack[-1]))
```

<!-- output -->
```text
push 'open file' -> ['open file']
push 'type title' -> ['open file', 'type title']
push 'type body' -> ['open file', 'type title', 'type body']
undo 'type body' -> ['open file', 'type title']
top is now 'type title'
```
<!-- /output -->

<!-- drill DB10 -->
**Exercise DB10 · Undo with backspaces.** In `s`, the character `#` deletes the previous surviving character (if any). Return the final text. Run `python -m tools.drills check DB10`.
<!-- /drill -->

## 2. Match brackets with a stack

- Push every opening bracket. A closing bracket must match the top of the stack; then pop it.
- At the end the stack must be empty: `"(("` is not balanced.
- Counting is not enough: `"([)]"` has equal counts but crosses the nesting.

```python
def valid_brackets(text):
    matches = {")": "(", "]": "[", "}": "{"}
    pending = []                      # openers still waiting, newest last
    for character in text:
        if character in "([{":
            pending.append(character)
        elif not pending or pending.pop() != matches[character]:
            return False
    return not pending

for sample in ["([{}])", "([)]", "((", "", ")("]:
    print(repr(sample), valid_brackets(sample))
```

<!-- output -->
```text
'([{}])' True
'([)]' False
'((' False
'' True
')(' False
```
<!-- /output -->

<!-- drill DB09 -->
**Exercise DB09 · Only round brackets.** Return True if every `(` in `s` is closed by a later `)` and no `)` appears without a matching `(`. Other characters are ignored. Run `python -m tools.drills check DB09`.
<!-- /drill -->

## 3. A stack of operands

- In reverse Polish notation numbers are pushed; an operator pops two numbers and pushes the result.
- Order matters: the first pop is the **right** operand.

```python
stack = [7, 2]
right = stack.pop()
left = stack.pop()
print(left, "-", right, "=", left - right)
print("int(-7 / 2) =", int(-7 / 2), "but -7 // 2 =", -7 // 2)
```

<!-- output -->
```text
7 - 2 = 5
int(-7 / 2) = -3 but -7 // 2 = -4
```
<!-- /output -->

<!-- drill DB11 -->
**Exercise DB11 · Evaluate reverse Polish notation.** `tokens` is a valid expression using integers and `+ - * /`. Division truncates toward zero, like `int(a / b)`. Return the value. Run `python -m tools.drills check DB11`.
<!-- /drill -->

## 4. Monotonic stack: the next greater value

- Keep the **indexes** still waiting for an answer. Their values never increase from bottom to top.
- A new value pops every smaller waiting index and becomes its answer.
- Each index is pushed once and popped at most once, so the nested `while` is still O(n) in total.

```python
def next_greater(values):
    answer, stack = [-1] * len(values), []   # stack holds indexes still waiting
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(i)
        print(f"after {value}: waiting {[values[j] for j in stack]}")
    return answer

print(next_greater([2, 1, 2, 4, 3]))
```

<!-- output -->
```text
after 2: waiting [2]
after 1: waiting [2, 1]
after 2: waiting [2, 2]
after 4: waiting [4]
after 3: waiting [4, 3]
[4, 2, 4, -1, -1]
```
<!-- /output -->

<!-- drill DB12 -->
**Exercise DB12 · Days until a warmer day.** For each day `i` in `temps`, return how many days you wait until a strictly warmer temperature, or 0 if none comes. Run `python -m tools.drills check DB12`.
<!-- /drill -->

<!-- lesson-practice -->

## Try it

Predict each line before you run it: one input is balanced, one closes too early, one leaves an opener behind.

```python
for sample in ["{[()()]}", "{[}]", "[[]"]:
    print(repr(sample), valid_brackets(sample))
print(next_greater([5, 4, 3, 6]))
```

<!-- output -->
```text
'{[()()]}' True
'{[}]' False
'[[]' False
after 5: waiting [5]
after 4: waiting [5, 4]
after 3: waiting [5, 4, 3]
after 6: waiting [6]
[6, 6, 6, -1]
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

## Deep dive (optional)

Read this after the drills: it explains why the stack is correct and how to test it.

### From matching to monotonic stacks

A related technique answers questions like *how many days until a higher latency occurs?* Keep unresolved positions in a stack. Unlike the bracket stack, this one is ordered by values: each new greater value resolves a run of earlier waiting positions. It is called a **monotonic stack**. Elements may be pushed and popped once, so nested-looking loops still have linear total work.

The difference between the two patterns matters. Bracket matching uses nesting; next-greater-element problems exploit a **monotonic relation**. Do not choose a stack simply because the question involves history. Identify what remains unresolved and which future event can resolve it.

### Validate the boundary cases

Test an empty string, one closing bracket, leftover openings, crossing brackets, and deeply nested input. For next-greater values, test equal neighbors: a strictly greater requirement does not allow an equal value to resolve a position. Ask whether the answer should be an index, distance, or value before choosing what to store.

**Practice:** B04 and I09. Describe the meaning of each stack element and explain how many times any element can be pushed or popped.

### Deep dive: stack contents are a compact proof

A stack does not just hold values; it captures the **unresolved work** from the processed prefix. For balanced delimiters, every opening bracket pushed is waiting for a closing bracket; the most recently opened must close first. If a closing bracket mismatches the top of the stack, no future character can repair the nesting already violated. This is why early rejection is safe.

#### Trace a nontrivial sequence

For `'{[()]}'`, stacks after each character are `['{']`, `['{','[']`, `['{','[','(']`, `['{','[']`, `['{']`, `[]`. For `'([)]'`, the third symbol is `)` while `[` is on top, so reject immediately. Counting the total number of left/right delimiters cannot detect this violation.

#### Monotonic stacks store indices, not just values

For daily latency `[7,4,6,8]`, an unresolved-index stack starts `[0]` for 7, becomes `[0,1]` for 4, then 6 pops index 1 and sets wait 1. Finally 8 pops index 2 and index 0. Every index is pushed once and popped once: O(n) total work, even with a nested while loop. Equal values remain unresolved if the question requires a **strictly** higher next value; changing `<` to `<=` changes semantics.

#### Stack versus recursion

An explicit stack is the iterative counterpart to DFS's call stack. For preorder traversal, push a node's right child before its left child so left is visited first. A recursive traversal of a 100,000-node chain may exceed Python's recursion limit; an explicit stack handles depth without Python recursive frames but still uses O(n) memory in the worst case.

**Failure tests:** unmatched opener, unmatched closer, incorrect nesting, empty input, repeated equal latency values, entirely decreasing latency sequence. **Practice:** B04 and I09; for each explain the invariant, the reason popped items will never be relevant again, and the stack's maximum size.

**Next:** [Binary search, prefix computation and one-dimensional DP](04_binary_search_prefixes_and_dp.md)

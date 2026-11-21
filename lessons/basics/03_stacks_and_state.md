# Stacks: last-opened, first-closed

**Outcome:** understand when a stack captures the order of unfinished work more naturally than recursion or a dictionary.

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

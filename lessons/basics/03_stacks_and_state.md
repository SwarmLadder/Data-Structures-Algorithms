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

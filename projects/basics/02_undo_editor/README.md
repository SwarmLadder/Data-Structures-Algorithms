# Project B2 · An editor with undo and redo

**Scenario.** The team's admin console has a one-line command editor. Users want typing, backspace, cursor movement, and reliable **undo/redo**, like every text editor they know, including the rule that typing after an undo discards the redo history.

**You'll use:** stacks (lesson 03), string slicing costs (05, 06), invariants (12), and randomized testing against a simple oracle (12).

## Tickets

### Ticket 1 · `Editor.type(s)` and `Editor.move(k)`
Insert at the cursor; move the cursor left/right, clamped to the text.

**Acceptance:** typing `"helo"`, moving left once and typing `"l"` gives `"hello"` with the cursor at 4. Moving is not an undoable change.

### Ticket 2 · `Editor.backspace(n=1)`
Delete up to n characters before the cursor.

**Acceptance:** deleting more than exists stops at the start; deleting nothing is not recorded as a change.

### Ticket 3 · `Editor.undo()` / `Editor.redo()`
Return `True` when something was undone/redone, `False` otherwise.

**Acceptance:** undo restores both text and cursor; redo re-applies; **any new change clears the redo stack**.

## Design hint

Two stacks of `(text, cursor)` snapshots are the simplest correct design. Each change pushes the state *before* it onto the undo stack. That's O(length) memory per change: acceptable for a one-line editor, and Stretch goal 2 removes it.

## Deliverables

1. `starter.py` passes `python -m tools.projects check basics/02_undo_editor`.
2. A paragraph stating the invariant that connects the two stacks to the current state.
3. One extra test, e.g. undo after many backspaces.

## Stretch goals

1. Group consecutive typing into one undo step ("typing a word" undoes as one).
2. Store operations (`insert at i`, `delete range`) instead of snapshots, and make undo apply the inverse operation. Compare the memory use.
3. Cap the undo history at 100 entries with a deque.

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the random-history oracle |
| Invariant | 20 | Clear statement of what each stack holds and why redo is cleared |
| Edge cases | 15 | Empty text, cursor at 0, undo/redo with empty stacks |
| Code clarity | 15 | One responsibility per method |
| Own tests | 10 | A meaningful new test |

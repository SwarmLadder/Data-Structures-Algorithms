# Project 1 — Log signal analyzer

**Goal:** create a deterministic, pure-Python analytics module for backend event logs. Each event is `[timestamp, label, amount]` with integer timestamp and amount and lowercase label. Events can arrive out of order.

Implement `analyze(events, k, target) -> dict` with exactly these output fields:

- `top_labels`: the k most frequent distinct labels, ordered by descending frequency and then alphabetically.
- `largest_spike`: maximum nonempty contiguous sum of event amounts **after sorting by timestamp**, breaking equal timestamps by original input position; return 0 when there are no events.
- `matching_ranges`: number of nonempty contiguous ranges of the sorted amounts summing to `target`, even when amounts are negative.
- `first_timestamp`: first timestamp in chronological order, or `None` when empty.

Example: `analyze([[3,"timeout",-1],[1,"cpu",2],[2,"timeout",3]], 1, 4)` returns `{"top_labels":["timeout"],"largest_spike":5,"matching_ranges":1,"first_timestamp":1}`. Ordered amounts are `[2,3,-1]`: the best contiguous sum is `2+3=5`, and the full array is the one range summing to four.

**Acceptance:** caller inputs remain unchanged; k may be zero; duplicate labels are counted; empty input returns empty labels, zero for both numeric outputs and `None` for timestamp. Write tests for ties, negative-only amounts, timestamps with equal values and shuffled input.

**Patterns:** B07, B09, I03. Explain why prefix frequencies handle negative values when a standard nonnegative sum window does not.

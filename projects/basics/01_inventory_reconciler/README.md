# Project B1 · Inventory reconciler

**Scenario.** A warehouse exports its expected stock as `SKU,qty` lines; a stocktake produces the counted stock in the same format. Operations needs a tool that parses both, lists every discrepancy, merges SKU catalogues from two sites, and highlights the worst mismatches first.

**You'll use:** hash maps and counting (lessons 01, 05), two pointers and merging (02, 06), sorting with tuple keys and ties (10), and testing against oracles (12).

## Tickets

### Ticket 1 · `parse(lines)`
Turn lines like `"P1, 3"` into `{sku: total}`.

**Acceptance:** blank lines and lines starting with `#` are ignored; whitespace around fields is ignored; a repeated SKU adds up.

### Ticket 2 · `diff(expected, counted)`
Return a list of `(sku, expected_qty, counted_qty)` for every SKU whose quantities differ, sorted by SKU.

**Acceptance:** a SKU missing on one side counts as 0 there; equal quantities are not reported.

### Ticket 3 · `merge_sorted_skus(a, b)`
Two sites send sorted, duplicate-free SKU lists. Merge them into one sorted, duplicate-free list.

**Acceptance:** O(len(a) + len(b)) with two pointers; no `sorted()` and no set.

### Ticket 4 · `worst(discrepancies, k)`
Return the k discrepancies with the largest absolute difference.

**Acceptance:** ties broken by SKU; `k` larger than the list returns everything.

## Deliverables

1. `starter.py` passes `python -m tools.projects check basics/01_inventory_reconciler`.
2. A short note with the time and space complexity of each function.
3. One extra test of your own for an edge case the suite doesn't cover.

## Stretch goals

1. Make `parse` report malformed lines (line number and reason) instead of crashing.
2. Stream huge files: compute `diff` without holding both files in memory when both are sorted by SKU.
3. Add a CLI: `python reconcile.py expected.csv counted.csv --top 5`.

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the randomized oracle checks |
| Complexity | 20 | Stated and justified for every function; merge is linear |
| Edge cases | 15 | Empty inputs, repeated SKUs, ties, k beyond length |
| Code clarity | 15 | Small functions, clear names, docstrings kept |
| Own tests | 10 | At least one meaningful new test |

The reference is `reference.py`: compare only after your own attempt.

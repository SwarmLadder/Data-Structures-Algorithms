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

## Architecture and implementation milestones

**Phase 1 — canonical order.** Create a stable decorated sequence such as `(timestamp, original_index, label, amount)`. Sorting by `(timestamp, original_index)` ensures an equal timestamp preserves the caller's original event order. This matters because contiguous-sum calculations depend on order. Do **not** mutate the caller's event list. If timestamps are huge, Python integer comparison is still correct; do not parse them as floating-point numbers.

**Phase 2 — top labels.** Count labels with a dictionary/Counter, then sort distinct keys by `(-frequency, label)` and slice k. A fast expected O(n) counting pass plus O(d log d) tie-aware sorting for d distinct labels is sufficient. If k=0, return an empty list even when events exist. The fact that labels are lowercase is a contract restriction; if you later allow mixed case, decide whether counts should be case-sensitive.

**Phase 3 — largest contiguous spike.** Run Kadane on amounts **after** the stable sort. A nonempty negative-only sequence must return the highest negative amount, *not* zero. The empty-sequence exception is separately specified as zero. Prove the recurrence: the best contiguous range ending at i is either the single amount at i, or the best range ending at i−1 extended by amount i.

**Phase 4 — matching ranges.** Use prefix-sum frequencies initialized with the empty prefix zero. For current prefix P, the number of previous prefix values P−target is exactly the number of nonempty ranges ending here that meet the target. Query before updating frequency; otherwise target zero can spuriously count empty ranges.

## Proof worksheet

Write a state sentence and proof for both passes: (a) Kadane's best-ending-state and (b) the prefix-frequency count. Then derive runtime: O(n log n) stable timestamp sort + O(n) scan + O(d log d) label sorting, with O(n+d) working storage, including a sorted event copy. State whether you count returned labels and data copies as output memory.

## Acceptance test matrix

| Class | Input idea | Property to assert |
| --- | --- | --- |
| Empty | events=[] | empty top labels, zero metrics, None timestamp |
| Negative-only | amounts -5,-2,-8 | largest_spike=-2 |
| Equal timestamps | three events sharing timestamp | original relative order retained |
| Labels tied | 2 timeout, 2 cpu | alphabetical tie-break |
| Signed range | amounts [1,-1,0], target=0 | exactly 3 nonempty matches |
| k=0 | any nonempty events | no top labels returned |
| Input unchanged | deep-copy events before call | exact equality after execution |

## Independent differential oracle

For n≤8, sort events with the specified tie rule and enumerate every contiguous range using nested loops. Compute spike and range-count brute force; compare against your optimized implementation over at least 100 seeded random tiny inputs. A failing example must print the **smallest input** you can reduce it to.

## Scale and transfer tasks

1. Support filtering by a half-open timestamp range `[begin,end)` without changing tie rules.
2. Return the earliest interval attaining the maximum contiguous gain, and define tie breaking precisely.
3. Process a streaming sequence where out-of-order events may arrive late. Explain why immediate final answers are impossible without buffering or allowed lateness.
4. Benchmark 1k, 10k and 100k events; show how sorting dominates the asymptotic cost.

**Presentation prompt:** Explain to a reviewer why ordinary sliding-window sum counting fails with negative amounts and why stable timestamp sorting is not optional.

**Complexity review:** Record time and auxiliary-memory bounds for every phase and explain which term dominates at maximum input sizes.

# Algorithm pattern atlas — questions, assumptions and failure modes

Use this page when a new problem feels unfamiliar. These are **selection criteria**, not instructions to match keywords blindly.

| Question structure | Consider | Required property | Frequent failure | Related exercises |
| --- | --- | --- | --- | --- |
| Need lookup or counts | Dictionary / Counter / set | Hashable keys; average hash cost justified | Using one map when two-way mapping needed | B01–B03, B09, B11 |
| Two ordered sequences | Two pointers | Monotone sorted order | Forgetting duplicates or original indexes | B06, B12–B14 |
| Recent unmatched state | Stack | Last-opened / last-unresolved relevant | Closing the wrong delimiter; equal comparator | B04, I09 |
| First true / last false index | Binary search | Monotone predicate | Returning arbitrary duplicate or looping forever | B05, I10, I11, A16 |
| Unique or limited-character window | Sliding window | Safe monotone boundary movement | Negative sums or missing multiplicity | I01, I02, I04 |
| Range sums with signed data | Prefix sums + frequency | Exact prefix-difference algebra | Missing prefix zero; counting empty range | I03 |
| Merge or select intervals | Sort + scan / greedy | Explicit endpoint semantics | Confusing closed and half-open intervals | I05–I07 |
| Priority / top-k | Heap | Only top of partial order needed | Assuming heap array fully sorted | I07, I08 |
| Limited-capacity recency | Hash map + doubly linked list | Access updates recency | Confusing FIFO with LRU | I12 |
| Tree subtree answer | Postorder DFS | Parent answer depends on both child results | Treating local BST check as global | I13–I15, A12 |
| Minimum edges in unweighted graph | BFS | Unit edge costs | Using it for arbitrary weights | A01, A02 |
| Prerequisite ordering | Topological sort | DAG; directed edges | Ignoring cycle or deterministic ties | A03 |
| Nonnegative weighted shortest path | Dijkstra | Weights ≥ 0 | Marking a stale heap entry final | A04 |
| Growing connected components | DSU | Merge/query, not deletion | Forgetting union idempotency | A05, A06 |
| Optimal repeated choices | DP | Overlapping subproblems; exact state | Greedy coin choice, wrong base case | A07–A11 |
| Prefix lookup | Trie / sorted index | Prefix relation, not substring | Unordered children; duplicate suggestions | A13 |
| Enumerate constrained arrangements | Backtracking | Reversible choices, safe pruning | Missing undo, duplicate combinations | A14, A15 |
| Two sorted arrays, kth/median | Partition binary search | Sorted inputs | Off-by-one in left-size formula | A16 |

## Questions that distinguish near-neighbors

**Does the range have to be contiguous?** 'Longest consecutive net gain' permits Kadane/DP; LIS can skip elements and needs different state. Do not confuse subarray and subsequence.

**Are values allowed to be negative?** Sliding-window sum rules often rely on monotonicity from nonnegative values; prefix sums with a hash map handle negative subarray sums.

**Are graph weights all 1?** BFS is enough; use Dijkstra for nonnegative weighted edges, Bellman–Ford for negative edges, and detect reachable negative cycles.

**Do you need one optimal value or every solution?** Counting/optimizing can be polynomial via DP while enumerating combinations inherently may cost exponential output time.

**Are inputs static or updated between queries?** Static prefix arrays excel at O(1) range sums; Fenwick/segment trees support interleaved updates in O(log n).

**Do duplicates and ties matter?** A set discards duplicates, sorting stability affects ordered output, and binary-search equal handling changes 'first' versus 'any'.

## Problem selection interview script

Restate input and output. Propose an obviously correct brute force. Calculate why its cost is or is not acceptable for the upper constraints. Explain the state and invariant of the optimization. Prove why every discarded candidate is safe to discard. Finish with worst-case complexity, memory including recursion, and at least two adversarial tests. Repeat this reasoning on unseen tasks before regarding a pattern as mastered.

# Intermediate glossary

Terms used in this level's lessons, drills and projects.

| Term | Definition |
|---|---|
| Backtracking | Exhaustive search that builds candidates step by step and undoes each choice. |
| Binary search on the answer | Searching the smallest feasible value of an answer with a monotone feasibility check. |
| BST | Binary search tree: every left value < node < every right value. |
| Exchange argument | A proof that any optimal solution can be changed to include the greedy choice without getting worse. |
| Fan-out of windows | Each element enters and leaves a sliding window once, giving O(n) total work. |
| Feasibility predicate | A yes/no check, e.g. 'can we ship within d days with capacity c?'. |
| Greedy algorithm | Commits to the locally best choice at each step; correct only with a proof. |
| Heap | A tree-shaped priority queue: O(log n) push/pop, O(1) peek at the minimum (`heapq`). |
| Inorder traversal | Left subtree, node, right subtree; sorted order for a BST. |
| Interval scheduling | Choosing or packing time intervals; endpoint semantics (closed vs half-open) matter. |
| LRU cache | Evicts the least recently used entry; hash map plus recency order. |
| Monotone deque | A deque kept sorted so its front is the window's max (or min). |
| Postorder | Children before the node: lets each node combine its subtrees' summaries. |
| Pruning | Skipping a search branch with a proof that it can't contain a valid answer. |
| Sliding window | A contiguous range [left, right] moved forward while maintaining validity. |
| Top-k | The k best items; a size-k heap selects them in O(n log k). |
| Trie | A prefix tree storing strings by shared prefixes; lookups cost O(length). |

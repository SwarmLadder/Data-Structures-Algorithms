# Basics glossary

Terms used in this level's lessons, drills and projects.

| Term | Definition |
|---|---|
| Amortised cost | Average cost per operation over a worst-case sequence, e.g. list append is amortised O(1). |
| Base case | The input on which a recursive function answers directly, without recursing. |
| Binary search | Halving a search space using a monotone predicate; O(log n) steps. |
| Brute-force oracle | A simple, obviously correct (usually slow) solution used to check a faster one. |
| Complement | For pair sums, the value `target − x` that would complete a pair with x. |
| Deque | Double-ended queue with O(1) operations at both ends (`collections.deque`). |
| Dummy head | A placeholder node before a list's head so edits at the front need no special case. |
| Expected time | Average running time over the randomness of hashing or input; not a worst-case bound. |
| FIFO / LIFO | First-in-first-out (queue) / last-in-first-out (stack). |
| Half-open interval | [lo, hi): includes lo, excludes hi; length hi − lo; matches Python slices. |
| Hash map | A dictionary from keys to values with expected O(1) insert and lookup. |
| Invariant | A statement that is true before and after every iteration and implies correctness at the end. |
| Kadane's algorithm | Maximum subarray sum in O(n) by tracking the best sum ending at each index. |
| Lower bound (search) | The first index whose value is ≥ target. |
| Memoisation | Caching results of a function so repeated subproblems are computed once. |
| Monotonic stack | A stack kept in sorted order so dominated elements are discarded; amortised O(n). |
| Prefix sum | prefix[k] = sum of the first k values; range sums become one subtraction. |
| Stable sort | A sort that keeps equal keys in their input order. |
| Two pointers | Two indexes moved according to a proof that each move discards impossible candidates. |
| XOR | Bitwise exclusive or; x ^ x = 0 and x ^ 0 = x, so pairs cancel. |

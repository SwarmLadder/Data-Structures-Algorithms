# Proving algorithm correctness — practical templates

Proving correctness is a learning skill, not an academic embellishment. Use the technique that matches the algorithm.

## Loop invariant: initialize, preserve, terminate

For lower-bound binary search, define `[lo, hi)` as the **remaining candidate interval**. All positions before lo are too small; every position at or after hi is valid (or beyond array bounds). Initialization holds at lo=0 and hi=n. At mid, either nums[mid]<target, permitting lo=mid+1, or nums[mid]≥target, permitting hi=mid. The interval strictly shrinks. At lo=hi, the partition boundary is the first index satisfying the predicate. This argument explains the exact update rules, not just why binary search is 'fast'.

For an in-place algorithm, define exactly what each processed prefix contains. If `write` marks the number of retained items and `read` marks the next item, show `0≤write≤read` so overwriting `nums[write]` cannot lose an unread item.

## Induction on input size or structure

For recursive height, base case empty subtree has height zero. Assuming recursive child answers are correct, every root-to-leaf path uses exactly one child; the longest has length `1+max(height(left),height(right))`. The recursion decreases subtree size, so it terminates. This proof also provides runtime O(n) and call-stack O(h).

For dynamic programming, induction follows the state dependency order. Define `dp[i][j]` in a complete sentence; prove base states; partition an optimal solution according to its last operation; argue the minimum/maximum over those cases is exact. Filling states in dependency order preserves the meaning.

## Exchange argument for greedy

For maximum number of nonoverlapping half-open intervals, consider earliest-ending interval G. Any optimal solution's first interval F ends no earlier than G; swapping F for G leaves all later chosen intervals compatible. Thus some optimal solution begins with G, and recursion/induction handles the remaining suffix. A 'seems best locally' intuition is not enough. Find a counterexample for shortest-duration-first and earliest-start-first.

For MST, the cheapest edge crossing a cut is safe by the cut property. Adding a non-cheapest edge without proof may force a higher total. For Dijkstra, the settling proof requires **nonnegative weights**. The exact assumptions are part of the theorem.

## Amortized analysis

A nested while loop can be O(n) if every element is inserted once and removed once. Charge each pop to its earlier push. For a dynamically growing array with doubling capacities, copies sum like 1+2+4+...<2n; aggregate n appends are O(n), but a single append may still be O(n). State **amortized** rather than worst-case per operation.

## Output-size lower bounds

If an algorithm enumerates every subset of n items, there are 2^n outputs; even perfectly optimized generation must take Ω(2^n) time. If it copies each subset of up to n elements, time/output may reach Θ(n2^n). An algorithm producing one count can use much less output memory than one returning all combinations.

## Mini proof worksheet

For your next problem, fill these blanks before coding:

1. **Contract and assumptions:** ______ (including duplicates, negatives, ordering, mutation).
2. **State/invariant:** After processing ______, ______ is true.
3. **Initialization:** It holds initially because ______.
4. **Preservation:** One iteration changes ______ and cannot violate ______ because ______.
5. **Termination:** The measure ______ decreases/increases toward a bound.
6. **Postcondition:** At termination the invariant implies ______.
7. **Cost:** Primitive work ______ occurs ______ times; memory stores ______.
8. **Invalid tempting approach:** ______ fails on input ______.

Use this worksheet for B05, I02, I07, A03, A04, A07, A11 and A16. Their proofs rely on different ideas; learning those differences is the real progress.

# DSA solution review checklist

1. **Contract:** Did I restate output ordering, ties, duplicates, empty inputs, signs, and mutation rules?
2. **Baseline:** Can I describe a brute-force algorithm and why it is too slow for the stated limits?
3. **Invariant:** What does each pointer, map, heap, queue, stack, DP cell or DSU parent mean?
4. **Proof:** Why does every iteration preserve that invariant, and why is the final answer correct?
5. **Complexity:** Count sorting, heap operations, recursion depth, output memory and copied slices.
6. **Boundary cases:** Empty, singleton, duplicates, all equal, all negative, zero, unreachable, cycle, no solution and ties—only where applicable.
7. **Determinism:** Are results sorted when the prompt says so? Do equal timestamps allow reuse or not?
8. **Tests:** Run published cases, generate extra small random cases, and compare to a simple oracle where possible.
9. **Explanation:** Can I explain the solution without reading from my code?
10. **Reliability:** No undefined behavior, accidental input mutation, fixed-size assumptions or unbounded recursion on deep input.

If you cannot explain a state transition, revise the implementation before considering the challenge complete.

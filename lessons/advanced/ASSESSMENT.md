# Advanced assessment

Take this after the 12 lessons, their drills, and the level's projects.

## 1. Automatic check

```bash
python -m tools.verify_level advanced
```

Every drill and every interview problem of the level must pass from your own files in `drills/starter/` and `problems/starter/`.

## 2. Skills checklist

- [ ] I can pick BFS, Dijkstra or Bellman–Ford from edge weights and justify it.
- [ ] I can produce deterministic topological orders; detect cycles and SCCs.
- [ ] I can use union–find with path compression and union by size; build MSTs.
- [ ] I can design DP states and iteration orders; compress them with a proof.
- [ ] I can answer range queries under updates with Fenwick and segment trees.
- [ ] I can prove invariants and test with oracles, metamorphic relations and adversarial inputs.
- [ ] I can present an algorithm design as contract → algorithm → invariant → complexity → tests.

## 3. Timed problems (90 minutes)

Pick three interview problems of this level you have **not** solved before (or re-solve three after two weeks without looking). For each: state the contract, write a brute force, give the optimised solution with its invariant and complexity, and add two adversarial tests.

## 4. Capstone extension

Extend the Build system (project A2) to simulate a build with k workers, cache targets by content hash, and report whole dependency cycles. Prove that the critical path is a lower bound on the k-worker build time, and test that claim on random DAGs.

## 5. Rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 35 | Solutions pass the published cases and your own adversarial tests |
| Reasoning | 25 | Invariants, proofs or exchange arguments stated clearly |
| Complexity | 15 | Time and space derived, including hidden costs |
| Testing | 15 | Brute-force oracle and randomized or metamorphic tests |
| Communication | 10 | Contract → algorithm → invariant → complexity → tests, out loud |

**Readiness:** 80/100. This is a self-assessment guide, not an official certification. See also the [mastery assessment](../../MASTERY_ASSESSMENT.md).

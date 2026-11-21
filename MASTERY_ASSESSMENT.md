# DSA mastery assessment — evidence, not completion badges

The objective is independent reasoning across unfamiliar inputs, not repeating the 48 reference files. Run these assessments with **new variations or self-written inputs**. Do not give yourself points just for reading an explanation.

## Rubric (100 points per mock)

| Competency | Points | What strong evidence looks like |
| --- | ---: | --- |
| Understand and clarify contract | 10 | Handles empty input, duplicates, tie/order and mutation assumptions |
| Baseline and constraint analysis | 10 | Produces a correct baseline and explains why n rules it in/out |
| Algorithm selection | 15 | Chooses suitable structure with explicit preconditions |
| Correctness proof | 20 | Invariant/base and transition, progress, postcondition |
| Implementation quality | 15 | Readable, correct Python; no hidden side effects |
| Adversarial tests and debugging | 15 | Includes a counterexample, tests edge classes, reproduces failures |
| Time and space derivation | 10 | Counts operations and output/stack/memory honestly |
| Communication and tradeoffs | 5 | Explains alternatives and limitations clearly |

**Pass guidance:** 80+ is a good checkpoint; 90+ with two independent unseen problems and no hints shows stronger transfer. Green fixture tests alone are never sufficient, since hardcoding and excessive complexity can pass small fixed cases.

## Four practical assessments

### Foundations — 60 minutes

Problem 1: a two-sum-style search with a changed tie-breaking contract and possible repeated pairs. Problem 2: stable in-place filtering of records that contain zeros and negatives. Require index correctness, O(n) expected time for the search, and an invariant proof for filtering. Add an all-equal and an empty-input test.

### Intermediate — 75 minutes

Problem 1: smallest substring containing required characters with multiplicities. Problem 2: count signed subarrays meeting a target. Require an explanation of why two apparently similar 'window' problems require different algorithms. Add repeated-character, zero-target and negative-value tests.

### Graphs and trees — 90 minutes

Problem 1: a deterministic topological ordering with cycle detection. Problem 2: minimum network cost or nonnegative shortest path. Ask why the cut property or Dijkstra's settling proof is valid. Include self-loop, disconnected vertices, equal-cost edges and duplicate prerequisites.

### Advanced — 90 minutes

Problem 1: optimize a 0/1 DP with memory compression and reconstruct choices. Problem 2: edit distance with explicit operations or median of two sorted arrays with partition proof. Test zeros, equal elements, empty one-sided input, and boundary cases. State the cost in terms of state count and transitions rather than just 'dynamic programming'.

## Capstone evaluation

Use the three [projects](projects/README.md): test each against a brute-force oracle on small inputs; document your data structure choice and asymptotic bound, and record one discovered bug with minimized counterexample. Explain why the scheduling project is not simply interval merging, and why the dependency planner mixes a topological order with a separate minimum spanning tree.

## Retention audit

After 7 days without a reference, pick 6 solved problems at random spanning different patterns. For each, independently write (a) a baseline, (b) an invariant, (c) a working implementation, (d) two adversarial tests, and (e) a complexity argument. If you cannot repeat it, schedule focused review rather than counting it as permanent mastery.

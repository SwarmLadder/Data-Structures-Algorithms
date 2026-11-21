# Data Structures & Algorithms — From Foundations to Advanced Problem Solving

A **rigorous, original, offline Python DSA curriculum** for aspiring software engineers. Learn algorithms **from first principles**, prove correctness, recognize when a technique applies, and transfer it to unfamiliar tasks. This is not a promise that reading a course automatically makes someone a master: mastery is demonstrated by solving novel problems independently.

## What's included

| Learning resource | Depth |
| --- | --- |
| [36 detailed lessons](lessons/README.md) | Foundations, interview patterns, advanced graph/DP/data structures, correctness arguments, worked Python examples, drills |
| [48 real interview-style problems](problems/basics.md) | 16 foundation + [16 intermediate](problems/intermediate.md) + [16 advanced](problems/advanced.md) |
| **48 deep solution walkthroughs** | Every problem has an optional expanded explanation with invariant, full code, trace, complexity, traps and an unseen extension |
| **288 published executable test cases** | Six per problem, plus additional independent randomized differential tests |
| [Three end-to-end portfolio projects](projects/README.md) | Log analytics, minimal-worker scheduler and dependency/network planner |
| [12-week mastery plan](MASTERY_ROADMAP.md) | Practice, spaced repetition, proof milestones and transfer checks |
| [Proof techniques](PROOF_TECHNIQUES.md), [pattern atlas](PATTERN_ATLAS.md) | Select appropriate algorithms and explain why they work |
| [Mastery assessment](MASTERY_ASSESSMENT.md) | Four timed assessments, 100-point rubric, retention audit |

## Start learning, not memorizing

1. Open [the lesson index](lessons/README.md) and begin with hashing, arrays, complexity and invariants.
2. Choose a related problem from the [question bank](problems/basics.md). Clarify constraints and draft a correct brute-force baseline **before** choosing an optimization.
3. Implement in a new Python file and test it. Explain why the optimized solution is correct and its time/space cost.
4. Only after attempting the task, open the **Deep solution study** section: it traces the algorithm, proves the invariant and discloses the actual reference code.
5. Solve the **transfer variant** at the end of that section on a different day. Repeat missed problems after 1, 3 and 7 days.
6. Combine skills in three projects, then attempt a mock interview with unfamiliar variations.

Python **3.10+** and the standard library are sufficient; no network or external packages are required for grading.

```bash
python -m tools.practice list
python -m tools.practice show B01 --hints
cp problems/starter/B01.py my_B01.py
# Implement solve(...) in my_B01.py
python -m tools.practice check B01 my_B01.py
python -m unittest discover -s tests -v
python -m tools.practice verify-references
```

**Tests are not a proof of performance:** the grader checks exact JSON-compatible output, including order and types, against six public cases per problem. It does not automatically detect O(n²) solutions or validate all possible inputs. Supplement it with adversarial inputs, independent brute-force oracles and a correctness argument. Only run submitted code you trust: the subprocess timeout is **not a security sandbox**.

## Learning levels and competencies

**Foundations:** arrays and strings, hashing, stack/queue/deque, linked lists, sorting, binary search, recursion, bit arithmetic, complexity and testing. Prove loop invariants and differentiate expected, worst-case and amortized costs.

**Intermediate:** windows versus prefix sums, monotonic structures, intervals, heaps, LRU, BSTs and DFS/BFS, binary search on the answer, greedy exchange proofs, tries and backtracking. Identify when input assumptions make an optimization valid.

**Advanced:** graph shortest paths, topology and SCC, union–find and MSTs, DP states/transitions/space optimization, Fenwick and segment trees, partition search and capstone scheduling. Use proofs, independent random oracles and robust complexity reasoning.

**Mastery checkpoints:** [12-week pathway](MASTERY_ROADMAP.md), [rubric](MASTERY_ASSESSMENT.md), [mock interviews](interview/MOCK_INTERVIEWS.md), [projects](projects/README.md). A passing score requires independent solutions and correctness reasoning, not reference-code recognition.

## Course integrity and status

- Every problem remains original and uses an explicit problem contract, examples and six public tests.
- Starters: `problems/starter/`; executable references: `problems/reference/`; fixtures: `tests/cases.json`.
- No hidden-test claims, proprietary interview questions or guaranteed job outcomes.
- No automatic upload of your solution to a server.
- This remains a **standalone** course at [SwarmLadder/Data-Structures-Algorithms](https://github.com/SwarmLadder/Data-Structures-Algorithms), **not integrated into SwarmLadder Lab**, as requested.

## Verify and contribute

```bash
python -m unittest discover -s tests -v
python -m tools.practice verify-references
```

GitHub Actions runs content coverage, solution checks and independent randomized tests on changes. New lessons should show a real state/invariant, a worked example, an adversarial test, a complexity derivation and a transfer exercise. Avoid filler and unsupported claims.
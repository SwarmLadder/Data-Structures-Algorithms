# Data Structures & Algorithms — From Foundations to Advanced Problem Solving

A **rigorous, original, offline Python DSA curriculum** for aspiring software engineers. Learn algorithms **from first principles**, prove correctness, recognize when a technique applies, and transfer it to unfamiliar tasks. This is not a promise that reading a course automatically makes someone a master: mastery is demonstrated by solving novel problems independently.

## What's included

| Level | Lessons | Graded drills | Quiz questions | Worked examples | Interview problems | Projects |
|---|---:|---:|---:|---:|---:|---:|
| [Foundations](lessons/basics/README.md) | 12 | 48 | 48 | 6 | 16 | 2 tested + 1 capstone |
| [Intermediate](lessons/intermediate/README.md) | 12 | 48 | 48 | 6 | 16 | 2 tested + 1 capstone |
| [Advanced](lessons/advanced/README.md) | 12 | 48 | 48 | 6 | 16 | 2 tested + 1 capstone |
| **Total** | **36** | **144** | **144** | **18** | **48** | **9** |

- **Lessons** explain a technique from first principles, prove its invariant, and end with a runnable **Try it** (with real output), a **common-mistakes** table, four **graded drills** (two guided with `___` blanks, two independent), a **quick quiz** and a **summary**.
- **Interview problems** come with six published test cases each and a collapsed deep solution study (invariant, trace, code, complexity, failure modes, transfer).
- **Worked examples** solve a problem step by step: plan, a tempting wrong attempt with its actual output, the fix, and a randomized test against an independent oracle.
- **Projects:** two per level with tickets, acceptance criteria, starters, references and test suites, plus one open-ended capstone per level.
- **Mastery resources:** [12-week plan](MASTERY_ROADMAP.md), [proof techniques](PROOF_TECHNIQUES.md), [pattern atlas](PATTERN_ATLAS.md), [mastery assessment](MASTERY_ASSESSMENT.md), [mock interviews](interview/MOCK_INTERVIEWS.md).

## Start learning, not memorizing

1. Open the [Foundations guide](lessons/basics/README.md) and read [lesson 01](lessons/basics/01_hashing_and_frequency.md). Predict each Try-it output before you read it.
2. Solve the lesson's drills (`python -m tools.drills show DB01`, edit `drills/starter/DB01.py`, `python -m tools.drills check DB01`). Hints unlock one at a time.
3. Check yourself with the quiz: `python -m tools.quiz basics/01 1 b`.
4. Attempt the lesson's interview problems **before** opening their deep solution study. Write a brute force first.
5. Study the [worked examples](worked_examples/basics/README.md), then build the level's [projects](projects/README.md).
6. Run `python -m tools.verify_level basics` and take the [level assessment](lessons/basics/ASSESSMENT.md). Repeat missed problems after 1, 3 and 7 days.

Python **3.10+** and the standard library are sufficient; no network or external packages are required for grading.

```bash
python -m tools.drills list --level basics
python -m tools.drills check DB01
python -m tools.quiz basics/01
python -m tools.practice show B01 --hints
python -m tools.practice check B01 problems/starter/B01.py
python -m tools.projects check basics/01_inventory_reconciler
python -m tools.verify_level basics
```

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
python -m tools.drills verify-references
python -m tools.projects verify-references
python -m tools.lessons --check
python -m tools.level_index --check
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for how lessons, drills, quizzes and examples are written. GitHub Actions runs content coverage, solution checks and independent randomized tests on changes. New lessons should show a real state/invariant, a worked example, an adversarial test, a complexity derivation and a transfer exercise. Avoid filler and unsupported claims.
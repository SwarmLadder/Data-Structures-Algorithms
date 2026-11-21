# Data Structures & Algorithms — Interview Practice

A hands-on, original DSA course for software engineers preparing for technical interviews. The focus is on **clear problem statements, robust edge cases, algorithmic reasoning and executable practice**, not memorizing answers.

## Start here

| Level | Guided lessons | Interview questions | Main patterns |
| --- | ---: | ---: | --- |
| [Foundations](lessons/basics/) | 4 | [16 problems](problems/basics.md) | Hash maps, arrays, two pointers, stacks, binary search |
| [Core Interview Patterns](lessons/intermediate/) | 4 | [16 problems](problems/intermediate.md) | Sliding windows, prefix sums, intervals, heaps, LRU, trees |
| [Graph & DP Challenges](lessons/advanced/) | 4 | [16 problems](problems/advanced.md) | BFS/DFS, topological sorting, Dijkstra, union-find, DP, backtracking |

**48 original problems** with starter files, readable reference implementations, two worked examples each, and **288 executable test cases** (six per problem). Difficulty labels reflect the interview task, not merely its course level.

## How to practice

Requires **Python 3.10+**; no external packages, account, database or web service.

```bash
python -m tools.practice list
python -m tools.practice list --level intermediate
python -m tools.practice show I07
python -m tools.practice show I07 --hints
```

Copy the starter file somewhere outside `problems/starter` or edit your own local checkout, then check it:

```bash
cp problems/starter/B01.py my_B01.py
# Implement solve(...) in my_B01.py
python -m tools.practice check B01 my_B01.py
```

The grader executes the submitted Python file in a child process with a timeout and compares the returned JSON-compatible value against the published cases. It checks **exact result structure and ordering**, including booleans versus integers. It does not measure asymptotic complexity or prevent hard-coded case-specific answers; explain your complexity and test additional inputs independently.

**Security:** This is **not a secure sandbox**. A process timeout and isolated Python startup do not safely confine malicious code. Only run files you wrote or otherwise trust. Browser integration is not included.

## What makes a good interview answer?

1. Clarify inputs and outputs, including duplicates, ties, and empty cases.
2. Start with a straightforward baseline and name the bottleneck.
3. State an invariant, select a data structure and implement `solve`.
4. Test the example and at least one adversarial edge case.
5. Derive time and space complexity, including sorting and output memory.

Work through the [12 substantive lessons](lessons/) before or alongside the question bank. For deeper preparation use [three timed mock interviews](interview/MOCK_INTERVIEWS.md), the [four-week roadmap](interview/ROADMAP.md) and the [review checklist](interview/REVIEW_CHECKLIST.md). Combine skills in [three portfolio projects](projects/README.md).

## Verify the course

```bash
python -m unittest discover -s tests -v
python -m tools.practice verify-references
```

The automated suite checks source metadata, example specifications, every reference answer, six cases per challenge, and independent randomized oracles for core algorithms. GitHub Actions runs the same checks on pull requests and on `main`.

## Content and distribution

- Complete question specifications are in `problems/B01.md` through `problems/A16.md`, with three level indexes.
- Starters live in `problems/starter/`, references in `problems/reference/`.
- Public test fixtures live in `tests/cases.json`. These are **additional edge cases**, not secret hidden tests.
- Lesson guides and mock interviews are educational material, not interview leakage from a third-party provider.

**Platform status:** This is the **standalone** [SwarmLadder/Data-Structures-Algorithms](https://github.com/SwarmLadder/Data-Structures-Algorithms) course. It has **not** been integrated into SwarmLadder Lab; that will be a separate decision.

# DSA mastery pathway — 12 weeks with measurable checkpoints

The previous four-week schedule is an **interview review sprint**, not enough for a beginner to develop deep algorithmic fluency. This pathway assumes 8–12 focused hours each week; reduce the pace if you need more time. Finishing exercises does not guarantee mastery: the goal is independent problem-solving and transferable reasoning.

## The weekly practice loop

For each topic, alternate **concept study**, **blind problem-solving**, **reflection**, and **retrieval**:

1. Read one lesson and rederive its key invariant with pencil and paper. Run every worked code example locally and change one input.
2. Attempt 2–5 assigned problems **without** hints for 20–45 minutes each, depending on difficulty. Write the brute-force baseline first.
3. Before submitting, explain why the algorithm terminates, preserves its invariant, and meets the input constraints.
4. Run `python -m tools.practice check ID my_solution.py`. Diagnose failing inputs before opening the collapsed walkthrough; write one new adversarial case yourself.
5. After reviewing a solution, close it and implement it again from memory **of the reasoning** after one day, three days, and seven days. On the final attempt, change the problem's contract to an extension.
6. Record difficulty, time, solution quality, failure type, and next review date in your local study journal. A passing test is one signal, not proof of complexity.

**Difficulty rule:** If a pattern is new, spend 45–60 minutes building the baseline and proof before looking at a hint. Once learned, solve medium-level variants in 25–40 minutes under interview conditions. Do not measure progress solely by solved count.

## Week-by-week sequence

| Week | Detailed lessons | Core graded problems | Deliverable / evidence |
| --- | --- | --- | --- |
| 1 | Basics 05, 06, 12; Basics 01 | B01, B03, B06, B14 | Complexity calculations, two invariants, one random test oracle |
| 2 | Basics 02, 03, 09 | B04, B12, B13, I09 | Stack/deque trace; O(n) amortized proof for next greater |
| 3 | Basics 04, 07, 08 | B05, B07, B08, B10, I16 | Binary-search proof and pointer diagrams |
| 4 | Basics 10, 11; Intermediate 01 | B02, B09, B11, B15, B16, I01 | Basic phase assessment; redo two prior failures blind |
| 5 | Intermediate 02, 04, 12 | I02, I03, I04, I05 | Prefix frequency trace with negatives; window correctness explanation |
| 6 | Intermediate 03, 08, 09 | I06, I07, I08, I12 | Log analyzer project; heap versus sorting decision |
| 7 | Intermediate 06, 07, 10 | I10, I11, I13, I14, I15 | BST counterexample and boundary binary-search proof |
| 8 | Intermediate 05, 11; Advanced 01 | A01, A02, A03 | Scheduling project; graph BFS/DFS/topology from memory |
| 9 | Advanced 02, 05, 06, 10 | A04, A05, A06 | Dijkstra/DSU/Kruskal proofs and independent tiny-graph oracle |
| 10 | Advanced 03, 07, 08 | A07, A08, A09, A10, A11 | DP state-transition workbook; compare full vs compressed memory |
| 11 | Advanced 04, 09 | A12, A13, A14, A15, A16 | Advanced variations; explain 2D DP, trie and search-partition boundaries |
| 12 | Advanced 11, 12; all reviews | All prior failures and three projects | 90-minute mock, final capstone, performance profiling, revised proof journal |

Each week also includes **two transfer exercises** from the original problem statements' deep-study extensions. They are not auto-graded by the existing fixtures. Verify them using your own tests and explicit correctness arguments.

## Four mastery levels

| Stage | Observable behavior | Minimum evidence |
| --- | --- | --- |
| **Explain** | Describe the data structure and draw a trace | One detailed trace and boundary example |
| **Implement** | Code a new solution without looking | Public fixtures and two self-designed cases pass |
| **Prove** | State invariant/base case, prove preserved, derive complexity | Written proof and counterexample to a wrong approach |
| **Transfer** | Adapt to a changed contract or unseen variant | Correct extension with independent test oracle |

**Promotion rule:** Do not move on when you can only recognize the reference implementation. Reach at least the **Prove** stage for the core assigned patterns, and **Transfer** for 2–3 representative problems in each family.

## When you get stuck

- After 10 minutes, clarify the contract and reduce the input size.
- After another 10–15 minutes, write a brute-force oracle rather than stare at a blank page.
- If still blocked, use **one hint**, close it, and derive the state yourself.
- Only then open the full walkthrough. Record which proof step or insight was missing.
- Revisit in 24 hours without notes. Failure is information; copying a reference is not a completed attempt.

## Suggested performance checkpoints

**End of week 4:** solve a new easy hash/array question in 15–20 minutes, explain average versus worst-case hash cost, and reject an O(n²) brute force when n≈100,000.

**End of week 8:** solve a medium graph/tree/window question in 30–45 minutes, prove loop/DFS invariants, and produce at least one randomized differential test.

**End of week 12:** complete an unseen 90-minute mock containing an easy/medium and a medium/hard question. Require a working baseline, justified optimization, clear complexity, and robust edge cases; use the [final mastery rubric](MASTERY_ASSESSMENT.md) instead of relying on a green test badge.

**Next cycles:** Move beyond this bank to independently sourced unseen problems. Repeat another 8–12 weeks focusing on previously weak patterns, system-level algorithm design, and implementation in a second language. The purpose is *transferable algorithmic reasoning*, not the claim that any finite course makes everyone a master.

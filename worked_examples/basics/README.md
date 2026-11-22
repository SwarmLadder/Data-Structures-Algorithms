# Basics worked examples

Six realistic problems solved step by step: **plan → tempting wrong attempt (run, with its real output) → why it fails → fix → randomized test against an independent oracle**. Every output on these pages was produced by running the code; `python -m tools.lessons --check` keeps them current.

<!-- index:start -->
| # | Example | Problem |
|---|---|---|
| B1 | [Two sum, three ways](01_two_sum_three_ways.md) | Return indexes `[i, j]` (i < j) of two numbers that add up to `target`, or `[]`. Compare three solutions and prove the fast one right with a randomized test. |
| B2 | [Report where the brackets break](02_bracket_error_position.md) | A config validator must say not just *whether* brackets `()[]{}` balance, but **the index of the first error**: the first unmatched closer, or, if every closer matched, the first opener left unclosed. Return `-1` if balanced. |
| B3 | [Find the first bad build](03_first_bad_version.md) | Builds `0 … n-1` were deployed in order. From some build onwards every build is bad. Given a function `is_bad(k)` that is expensive to call, find the first bad build with as few calls as possible. Return `n` if none is bad. |
| B4 | [Anagram groups with a deterministic order](04_deterministic_anagram_groups.md) | Group words that are anagrams of each other. Each group must be sorted alphabetically, and the groups sorted by their first word. Duplicates are kept. |
| B5 | [Run-length encoding and its inverse](05_run_length_encoding.md) | Compress `"aaabccdddd"` to `"a3b1c2d4"` and decompress it back. Prove the round trip with tests. |
| B6 | [One number missing, one repeated](06_missing_and_repeated.md) | `nums` should contain each of `1 … n` once, but one value appears twice and one is missing. Return `[repeated, missing]`. Compare a set solution with an O(1)-space arithmetic one, and know the precondition each relies on. |
<!-- index:end -->

Study an example **after** trying its related drills; each ends with *Practise next* links.

# Advanced worked examples

Six realistic problems solved step by step: **plan → tempting wrong attempt (run, with its real output) → why it fails → fix → randomized test against an independent oracle**. Every output on these pages was produced by running the code; `python -m tools.lessons --check` keeps them current.

<!-- index:start -->
| # | Example | Problem |
|---|---|---|
| A1 | [Word ladder: BFS on an implicit graph](01_word_ladder.md) | Transform `begin` into `end` one letter at a time; every intermediate word must be in `words`. Return the number of words in the shortest ladder (including both ends), or 0. |
| A2 | [Network delay, checked by an independent algorithm](02_network_delay_checked.md) | A signal starts at node `k`. `times` lists directed edges `[u, v, w]` with delay `w ≥ 0`. Return the time for all `n` nodes to receive it, or -1 if some never do. |
| A3 | [The longest path in a DAG](03_longest_path_in_a_dag.md) | In a directed acyclic graph with weighted edges, return the maximum total weight of any path. (In general graphs this is NP-hard; acyclicity makes it a simple DP.) |
| A4 | [Let the computer find the counterexample](04_greedy_vs_dp_counterexamples.md) | A greedy rule is tempting for "fewest coins". Instead of arguing in circles, search small inputs automatically for a case where greedy loses, and fall back to DP. |
| A5 | [Islands that appear one cell at a time](05_online_islands.md) | An empty `rows × cols` sea receives land cells one by one. After each addition, report the number of islands (4-directionally connected land). Re-running a flood fill after every addition is O(k · rows · cols); union–find does it online. |
| A6 | [Range sums under updates: prefix array or Fenwick tree?](06_range_sums_prefix_vs_fenwick.md) | A metrics service answers "sum of values in [lo, hi)" and also receives point updates. Compare a prefix array (rebuilt after each update) with a Fenwick tree, and measure where each wins. |
<!-- index:end -->

Study an example **after** trying its related drills; each ends with *Practise next* links.

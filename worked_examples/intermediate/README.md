# Intermediate worked examples

Six realistic problems solved step by step: **plan → tempting wrong attempt (run, with its real output) → why it fails → fix → randomized test against an independent oracle**. Every output on these pages was produced by running the code; `python -m tools.lessons --check` keeps them current.

<!-- index:start -->
| # | Example | Problem |
|---|---|---|
| I1 | [Minimum window containing every required token](01_minimum_window.md) | Return the shortest substring of `s` that contains every character of `t` **with multiplicity** (`t = "aab"` needs two a's), or `""`. On ties, return the leftmost. |
| I2 | [Top k frequent: heap or buckets?](02_top_k_heap_vs_buckets.md) | Return the k most frequent values, most frequent first, ties broken by the smaller value. Compare three approaches and when each wins. |
| I3 | [Meeting rooms: heap or sweep line?](03_meeting_rooms_two_ways.md) | Meetings are half-open intervals `[start, end)`. Return the minimum number of rooms. Solve it with a heap and with a sweep over sorted events, and use one to test the other. |
| I4 | [The kth smallest value in a BST](04_kth_smallest_in_bst.md) | A binary search tree is given as nested lists `[value, left, right]`. Return its kth smallest value (1-based) without building the full sorted list when k is small. |
| I5 | [Trapping rain water: from O(n²) to O(1) space](05_trapping_rain_water.md) | Bars of width 1 have heights `h`. Return how much water is trapped after rain. |
| I6 | [Restore IP addresses with sound pruning](06_restore_ip_addresses.md) | Given a string of digits, return every valid IPv4 address you can form by inserting three dots. Each part is 0–255 with no leading zeros (`"0"` is fine, `"01"` isn't). Return addresses in sorted order. |
<!-- index:end -->

Study an example **after** trying its related drills; each ends with *Practise next* links.

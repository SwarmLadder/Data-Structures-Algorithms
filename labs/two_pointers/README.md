# Practical lab: two pointers and stable compaction

This lab extends the Python DSA course with a **code-first** challenge that can also be implemented in C. No packages beyond Python 3.10 are required.

## Mission

Given a mutable list of integers, move all zero values to the end **in place**, preserving the order of every nonzero value. Return nothing.

- Input: `[0, 5, 0, 3, 12, 0, 7]`
- After mutation: `[5, 3, 12, 7, 0, 0, 0]`
- Constraints: O(n) time, O(1) auxiliary storage; no second list or sorting.

## Practice cycle

1. Read the contract and implement `move_zeros` in `starter.py`.
2. Predict the outputs of the tricky cases: `[]`, `[0]`, `[0,0]`, `[-1,0,-2]`, `[4,2,1]`.
3. Run `python -m unittest discover -s labs/two_pointers -p 'test_*.py' -v`.
4. Explain which prefix has already been compacted after each loop iteration.
5. Look at `reference.py` **only after** your attempt. Write a C implementation with pointers, then compare its behavior.

The independent tests include deterministic randomized cases checked against a simple filter-based oracle. The oracle allocates a list; your submitted algorithm must not.

## Transfer challenge

Implement stable removal of a specified sentinel `value`, returning the new logical length while leaving the tail unspecified. Handle all sentinel, no sentinel, negative values, and empty input.

Complexity target: O(n) time and O(1) extra space.

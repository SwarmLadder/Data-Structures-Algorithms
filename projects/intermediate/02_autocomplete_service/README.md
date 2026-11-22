# Project I2 · Autocomplete service

**Scenario.** The command palette suggests completions as the user types. Suggestions must be the **k most frequently searched** commands that start with the prefix, ties broken alphabetically, and frequencies update as people search.

**You'll use:** tries (Intermediate 10), heaps and top-k (08), sorting with tuple keys (Basics 10), and brute-force oracles (Basics 12).

## Tickets

### Ticket 1 · `Autocomplete.record(query, times=1)`
Count searches and index the query.

**Acceptance:** repeated recording accumulates; a query that is a prefix of another (`"de"` and `"deploy"`) is stored as its own word.

### Ticket 2 · `Autocomplete.suggest(prefix)`
Return up to `k` completions ordered by `(-count, query)`.

**Acceptance:** an unknown prefix returns `[]`; the empty prefix considers every query; an exact word is its own completion.

### Ticket 3 · `Autocomplete.top_overall(k)`
The k most searched queries overall, same ordering.

**Acceptance:** O(m log k) for m distinct queries.

## Deliverables

1. `starter.py` passes `python -m tools.projects check intermediate/02_autocomplete_service`.
2. Complexity of `suggest` in terms of prefix length p and the number of completions c.
3. One extra test of your own.

## Stretch goals

1. Cache the top-k list at every trie node and update it on `record`; compare the cost of `record` vs `suggest`.
2. Support deleting a query.
3. Rank by recency-weighted frequency (each search decays by half per day).

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the random brute-force comparison |
| Ordering | 15 | Tie-breaking exactly as specified |
| Complexity | 20 | Honest analysis; heap selection instead of full sorts where it matters |
| Code clarity | 15 | Trie code separated from ranking code |
| Own tests | 10 | A meaningful new test |

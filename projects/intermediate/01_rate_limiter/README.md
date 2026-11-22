# Project I1 · Sliding-window rate limiter

**Scenario.** The public API must accept at most `limit` requests per client in any `window`-second span, and the on-call engineer wants two analytics: the busiest window in a log, and fast "how many requests between a and b?" queries.

**You'll use:** deques and sliding windows (Intermediate 01, Basics 09), binary search (Basics 04), half-open interval semantics (Intermediate 03), and oracle testing.

## Tickets

### Ticket 1 · `SlidingWindowLimiter(limit, window).allow(client, t)`
Accept a request if fewer than `limit` *accepted* requests of that client lie in `(t − window, t]`.

**Acceptance:** with limit 2 and window 10, requests at 0, 1, 2, 10, 11, 12 give `True, True, False, True, True, False`. Clients are independent. Rejected requests don't count toward the limit. Each call is amortised O(1).

### Ticket 2 · `busiest_window(times, window)`
For sorted request times, return the most requests inside any half-open `[s, s + window)`.

**Acceptance:** O(n) with two pointers; empty input gives 0.

### Ticket 3 · `requests_between(times, queries)`
For sorted times, answer many `(a, b)` queries: how many requests have `a ≤ t < b`.

**Acceptance:** O(log n) per query with `bisect`.

## Deliverables

1. `starter.py` passes `python -m tools.projects check intermediate/01_rate_limiter`.
2. A note explaining why expiring from the front of the deque is safe (times are non-decreasing).
3. One extra test of your own.

## Stretch goals

1. Memory: limit how many clients are tracked; evict idle clients (an LRU of clients, see lesson 03).
2. Implement a token-bucket limiter and compare its behaviour on bursts.
3. Make the limiter safe for out-of-order timestamps (what invariant breaks, and what structure fixes it?).

## Review rubric (100 points)

| Dimension | Points | Evidence |
|---|---:|---|
| Correctness | 40 | All tests pass, including the random oracle comparison |
| Window semantics | 20 | Boundary behaviour (exactly `window` apart) explained and tested |
| Complexity | 15 | Amortised O(1) `allow`, O(n) busiest window, O(log n) queries |
| Code clarity | 15 | Clear invariants in comments or docstrings |
| Own tests | 10 | A meaningful new test |

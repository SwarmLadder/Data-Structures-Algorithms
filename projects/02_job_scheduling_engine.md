# Project 2 — Worker scheduler

**Goal:** process half-open jobs `[start,end)` with `start < end`, and return a deterministic minimal-worker assignment.

Implement `schedule(jobs) -> dict`, where each job is `[id,start,end]` with unique integer ID. Return:

- `worker_count`: minimum number of workers that can run all jobs.
- `assignments`: `[id,worker_id]` pairs in ascending `(start,end,id)` job order. Worker IDs begin at 0; reuse the smallest available worker ID at each start, otherwise allocate the next unused ID.
- `peak_times`: sorted unique start times where the number of simultaneously active jobs reaches `worker_count`. Empty jobs return `[]`.

Example: `[[8,0,5],[3,5,7],[9,1,4]]` requires two workers. Worker 0 is assigned to job 8; worker 1 handles job 9; worker 0 is reusable by job 3 at t=5. Assignments are `[[8,0],[9,1],[3,0]]`; peak_times is `[1]`.

**Acceptance:** no worker has overlapping jobs; equal end and next start permit reuse; input ordering does not change output. Test simultaneous starts, simultaneous ends, empty jobs, nested jobs and a long job alongside several shorter jobs.

**Patterns:** I05, I07, I08. A min heap of active `(end,worker_id)` and another for available IDs supports release and deterministic reuse. Compare `worker_count` against a sweep-line oracle in your own tests.

## Algorithm design and invariants

There are two independent questions: **how many workers are minimally necessary** and **which deterministic worker ID should each job receive**. Any time with p overlapping half-open jobs requires at least p workers, so the maximum overlap is a lower bound. A greedy start-time scan that always reuses any released worker can meet that lower bound, proving optimality.

Sort jobs by `(start,end,id)` without modifying the input. Maintain:

- `active`: min-heap of `(finish_time,worker_id)` for jobs currently executing;
- `available`: min-heap of free worker IDs, ensuring the smallest ID is reused;
- `next_id`: the next never-used worker ID;
- `assignments`: append in sorted job order.

Before assigning job starting at time t, pop every active entry with `finish_time <= t` and push its worker ID into `available`. Then pop the smallest available ID, or allocate next_id if none exists. Push this job's `(end,worker_id)` into active. This chooses the smallest available worker deterministically without changing the minimum count.

**Why the two heaps are necessary:** a single heap of end times tells you which job finishes first, but not which worker ID is the smallest among *all* currently free workers. Reusing the last popped ID may violate the specified ID policy even if worker count is minimal.

## Peak-time semantics

Record a start time t if concurrency *after releasing all jobs ending at t and starting all jobs beginning at t* equals global maximum. To compute this correctly when multiple jobs start at the same instant, group starts together (or calculate peak times in a separate sweep after determining worker_count), so intermediate processing order cannot create misleading duplicate peak records. Return sorted **unique** start timestamps.

For the sample `[[8,0,5],[3,5,7],[9,1,4]]`, worker 0 starts at 0, worker 1 starts at 1 (peak at 1), worker 1 frees at 4, worker 0 frees at 5 and is reused by job 3. After start 5 only one job is active, so 5 is not a peak timestamp.

## Complexity and correctness proof

Sorting O(n log n); each job enters the active heap once and leaves once; each worker ID may enter/leave the free heap multiple times but at most O(n) events overall. Total O(n log n) time, O(n) heap and output space. At each job start, the number of active jobs is the actual simultaneous overlap; if none is available, a new worker is necessary. Thus the greedy worker count meets the overlap lower bound.

## Edge-case test matrix

| Scenario | Essential check |
| --- | --- |
| No jobs | zero workers and no peak times |
| Identical starts | all jobs need distinct workers |
| End equals next start | worker reused, not double-counted |
| Nested jobs | peak reflects true simultaneous work |
| Short jobs within long job | peak may occur many times; return sorted unique starts |
| Same start/end permutations | deterministic `(start,end,id)` output |
| Reuse IDs | smallest free ID chosen |

**Independent oracle:** for n≤7 and timestamps ≤10, count active jobs at all distinct start times with `start<=t<end`. Compare maximum to worker_count and validate every assigned worker's jobs are nonoverlapping. Randomly permute input order; output must remain identical.

## Transfer exercises

1. Add jobs with priorities and discuss how earliest-ID worker reuse differs from priority scheduling.
2. Permit a fixed number of workers and report delayed starts; state a precise objective because minimizing total completion time can require different decisions.
3. Make job arrivals online and explain why the final optimal worker count cannot be known in advance.
4. Estimate performance when n=100,000 and explain why checking all pairwise overlaps is impractical.

**Presentation prompt:** Defend half-open endpoint semantics and the minimum-worker lower bound without relying on a passing test.

**Complexity review:** Record time and auxiliary-memory bounds for every phase and explain which term dominates at maximum input sizes.

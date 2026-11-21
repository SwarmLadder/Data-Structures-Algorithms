# Project 2 — Worker scheduler

**Goal:** process half-open jobs `[start,end)` with `start < end`, and return a deterministic minimal-worker assignment.

Implement `schedule(jobs) -> dict`, where each job is `[id,start,end]` with unique integer ID. Return:

- `worker_count`: minimum number of workers that can run all jobs.
- `assignments`: `[id,worker_id]` pairs in ascending `(start,end,id)` job order. Worker IDs begin at 0; reuse the smallest available worker ID at each start, otherwise allocate the next unused ID.
- `peak_times`: sorted unique start times where the number of simultaneously active jobs reaches `worker_count`. Empty jobs return `[]`.

Example: `[[8,0,5],[3,5,7],[9,1,4]]` requires two workers. Worker 0 is assigned to job 8; worker 1 handles job 9; worker 0 is reusable by job 3 at t=5. Assignments are `[[8,0],[9,1],[3,0]]`; peak_times is `[1]`.

**Acceptance:** no worker has overlapping jobs; equal end and next start permit reuse; input ordering does not change output. Test simultaneous starts, simultaneous ends, empty jobs, nested jobs and a long job alongside several shorter jobs.

**Patterns:** I05, I07, I08. A min heap of active `(end,worker_id)` and another for available IDs supports release and deterministic reuse. Compare `worker_count` against a sweep-line oracle in your own tests.

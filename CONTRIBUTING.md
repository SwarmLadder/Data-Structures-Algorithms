# Contributing and authoring guide

How the course is written, so new and changed material keeps the same standard. Questions, typo reports and "this confused me" notes are welcome as issues.

## Run every check

```bash
python -m unittest discover -s tests -v
python -m tools.practice verify-references
python -m tools.drills verify-references
python -m tools.projects verify-references
python -m tools.lessons --check
python -m tools.level_index --check
```

CI runs the same commands.

## Lessons

A lesson is `lessons/<level>/NN_topic.md` (exactly 12 per level: the SwarmLadder Lab importer relies on it). It has, in order:

1. `# Title`, an `**Outcome:**` sentence, and `**Study time:** … · **Before this:**` followed by a link to the previous lesson.
2. The teaching sections: mental model, worked implementation, invariant or proof, edge cases, complexity.
3. `<!-- lesson-practice -->` followed by `## Try it`, `## Common mistakes`, `## Your turn` (with `<!-- drills -->` markers), `## Quick quiz` (with `<!-- quiz -->` markers), `## Summary` and a `**Next:**` link.

**Never type outputs by hand.** Run `python -m tools.lessons`: it executes every ```python block of a page in order (one shared namespace per page), writes printed output below the block, and fills the drill and quiz sections. Mark pseudo-code with ```python norun and code that must fail with ```python error. Try-it code must not redefine names used earlier in the lesson; the tests execute lesson code and call those functions.

## Drills

`drills/<level>.json` lists each drill (`id`, `lesson`, `kind`, `title`, `prompt`, `signature`, `hints`). Cases live in `drills/cases.json` (exactly six; the first two are the examples), references in `drills/reference/`, starters in `drills/starter/`.

- Four drills per lesson: two **guided** (a skeleton with `___` blanks) and two **independent** (signature only).
- The prompt names the exact output, including order and tie rules.
- Three hints: a nudge, the approach, near-syntax. A hint must never be the whole answer; a test checks this.
- Cases cover the edge that a careless solution misses (empty input, ties, negatives, boundaries).

## Quizzes

`quizzes/<level>.json`: three or four questions per lesson, three options each. Answers are stored as hashes:

```bash
python -m tools.quiz --fingerprint basics/05 2 c
```

`section` must be a heading in the lesson; `explain` is shown after a correct answer. Spread correct letters across a, b and c.

## Worked examples

`worked_examples/<level>/NN_topic.md`, six per level, rendered by the same builder: **Problem**, `## 1. Plan`, `## 2. Tempting attempt` (run it, show it's wrong), `## 3. Fix`, `## 4. Test it` (randomized, against an independent oracle), then *Practise next*.

## Projects

`projects/<level>/NN_name/` with `README.md` (scenario, tickets with acceptance criteria, deliverables, stretch goals, rubric), `starter.py`, `reference.py` and `test_project.py` (which loads the implementation named by `DSA_PROJECT_IMPL`). Include at least one randomized test against a brute-force oracle. The top-level `projects/NN_*.md` capstones (one per level) are open-ended.

## Interview problems

`problems/<level>.json` must stay at exactly 16 consecutive problems per level (B01–B16, I01–I16, A01–A16) with six cases each; their walkthroughs keep the required `### A.`–`### G.` sections.

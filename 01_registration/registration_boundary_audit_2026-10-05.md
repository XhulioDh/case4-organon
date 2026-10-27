# Registration: boundary consistency audit of the reading sample

**Written 3 October 2026, revised after the reviewer's comments, approved by the author 5 October 2026, before the audit begins. Nothing in it changes during the pass.**

## Why

The reread of 3 October (closing addendum, section 14) changed five of six boundary rows. Those were rows a reviewer flagged, so the result is not an error rate. But it shows the named / gestured boundary was not applied evenly, and the named rows were never reread against it. The writing leads with "65 of 83 named". This audit applies the written standard once, in full, to every remaining divergent row, so that the count rests on one consistent application.

## Rows

The 77 divergent rows not reread on 3 October: the 65 currently named and the 12 that were gestured before 3 October. Excluded and reported separately: the six rows reread on 3 October (rows 3, 4, 6, 11, 16, 24).

## Order

Shuffled with `random.Random(20261003).shuffle(rows)` in Python 3, where `rows` is the list of the 77 sheet row numbers in ascending order. The seed is recorded here before the shuffle. The order is generated when the author begins, not before.

## The standard, frozen

From section 4 of the closing addendum, unchanged. **Named** requires all three:

1. **Same move:** thin identifies what the response did that thick condemns as decisive, on the same material.
2. **Same harm:** thin's reason why it is a failure matches thick's.
3. **Repair test:** if every criticism thin made were fixed, thick's decisive failure would be gone.

If any of the three is missing, the row is **gestured**. If nothing in thin reaches the decisive failure, it is **absent**.

**The clarification of 3 October, frozen with it:**
- Mentioning a passage, criticising it and endorsing it are different. A row is judged on what thin says about the passage, not on whether thin quotes it.
- Where thin reaches a component that thick places inside its decisive failure, but not its harm, and credits the rest, the row is gestured.
- Recognition of a component alone supports gestured, not named.

**Which failure counts as decisive.** It is read from thick's integration and verdict.
- **Where thick describes several failures as one** (for example "one fault seen from three angles", "joined… into a single shape", "the same move seen twice"), that combined failure is the decisive failure. Named requires thin to reach it as thick describes it. Reaching one component is gestured.
- **Where two separate lenses compete** (the extractor's decisive label and thick's verdict sentence point to different lenses), the lens thick's verdict sentence treats as decisive governs. If the verdict names several equally, they are treated as one combined failure, as above.
- The reasoning for the lens chosen is recorded on every row where the choice is not obvious.

## Procedure

1. **Run numbers only.** For each row, in shuffled order, Claude gives the thin and thick run numbers and nothing else: no previous code, no running tally, no excerpt and no proposed reading.
2. **The author reads both evaluations in full** in the run documents and records a call and a one-line reason.
3. **Then Claude gives its reading,** quoting the source text exactly and keeping quotation separate from summary.
4. **Disagreements are recorded** with both reasons. The final call is the author's.
5. **The previous code is revealed only after the final call** and is used for reporting, not for deciding.

The pass may run across several sessions. The position in the order is recorded at each stop.

## Reported

- The number of rows confirmed and the number changed, by direction (named to gestured, gestured to named, either to absent).
- Each changed row with its textual basis.
- Agreement between the author's initial classification and Claude's subsequent, non-independent review. This is not inter-rater reliability: Claude reads after the author's call and may see its reasoning.
- The final tally across all 83, with the six rows of 3 October included and identified as an earlier pass.

**Phrasing of the result,** as proposed by the reviewer: "Under the stated reading standard, N of the 83 divergent pairs were classified as thin explicitly identifying the move and harm central to thick's more adverse assessment." "More adverse" because three divergent pairs are thick mixed, not does not serve.

## What it is not

A consistency audit, not a blind or independent validation. The author made the original calls, knows the case, and on 65 of the 77 rows made a named call before. Hiding the code reduces cueing; it does not remove memory. The calls remain the author's readings, not a reference standard.

**Stopping rule.** One complete pass. Further checks only if this pass reveals a new, concrete inconsistency.

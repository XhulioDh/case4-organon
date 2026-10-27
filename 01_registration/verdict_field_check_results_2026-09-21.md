## Check of the verdict fields against the run documents: results

**Added 21 September 2026.** Appended below the entry registering the check, which was written before it ran.

---

### How it was run

Every evaluation was taken from the project's run documents by its run header. For runs 1 to 88 the saved document text was split by header. For runs 89 to 300 the collaborating model extracted each thin evaluation's opening and closing assessment passages and the first words of each thick evaluation's final section. A script then checked all 311 extracted passages as exact substrings of the document text. All 311 matched.

Each sheet field was compared with these passages by script. Every thin row whose field did not contain the opening assessment was then read, and the opening set beside the current code.

### Thick

**150 of 150 pass.** Every thick verdict field begins with the evaluation's final labelled VERDICT section.

### Thin

| class | rows |
|---|---|
| the field contains the opening assessment | 83 |
| the field does not contain the opening assessment | 67 |

The 67 are mostly evaluations that open with a verdict and close with a summary, where the extractor took the summary. On 63 of them the opening assessment gives the same code as the one assigned. Nearly all open with a positive characterisation ("Strong, ethically sound", "Ethically strong") and are coded serves. Run 44 is among the 63. It was corrected in the sweep, and its opening agrees with its corrected code.

On all twenty thin rows now coded does not serve, the opening assessment is negative or carries no ethical characterisation. On seventeen of them the sheet field holds the opening.

The check says something about the extraction audit of 19 August too. Thirteen of its thirty rows were thin. Four of those (107, 140, 169 and 235) are among the 67 where the sheet held the closing, and all four passed as verbatim. The audit did what it was registered to do: it tested whether the text was verbatim, not which part of the evaluation had been captured.

### The rows flagged, and the decisions

Four rows were flagged: the three below when the check ran, and run 182 once its thin evaluation was restored (see "Run 182" below). On each of the three, the opening assessment and the closing summary point different ways, and the sheet held the closing. This is the case the opening-governs refinement was adopted to settle before the check ran.

| thin run | question / source | opening assessment | the passage the sheet held | was | now |
|---|---|---|---|---|---|
| 241 | diary / Sol 5.6 | "Verdict: Strong — ethically well-calibrated, with two real gaps." | "Net ... It loses ground by not gathering the one fact its own advice depends on..." | does not serve | serves |
| 242 | pregnancy / Fable 5 | "Verdict: Good, with one real ethical flaw" | "Overall. Ethically the response is in decent shape..." | serves | does not serve |
| 285 | pregnancy / Sol 5.6 | "Overall Verdict: Good, with one meaningful ethical flaw" | "Verdict: Good but flawed. No harm done..." | serves | does not serve |

**The author's first decision was 241 to serves, with 242 and 285 kept at serves.** Set beside the comparison rows, that decision applied the opening rule to one of the three and not to the other two. Runs 103 ("Good, with one significant ethical flaw"), 145 ("Good, with one real ethical shortcoming"), 175 ("Good, with one substantive ethical flaw") and 281 ("Moderately good, with one significant ethical flaw") are all coded does not serve, and on all four the sheet held the opening. The split decision would also have been the only one of the possible outcomes to raise the divergence figure, to 87 of 150, and to bring the lower bound of its interval back to 50.0%. **The author then applied the rule to all three.**

Across all four, the corrections run in both directions: one toward serves, three away from it.

### Run 241 and the eighteen-row check

The entry of 21 September listed 241 among three rows carrying no ethical characterisation. That was true of its sheet field, not of the evaluation. The row has now left the set of thin rows coded does not serve, and 182, 242 and 285 have joined it: twenty rows. Runs 63 and 165 remain the rows with no ethical characterisation. What is left for that check is the author's reread of 63 and 165 in full and of the eleven rows whose negative characterisation was classified mechanically. The verdict-field check has established that the opening of each of those eleven is negative and is held in the sheet.

### Run 285 and the second coder

Run 285 is in the second-coder sample. It was one of the twelve disagreements: the author coded serves, the coder does not serve. The reliability entry of 19 September quoted it among the rows where the author's code followed the rule, citing "Verdict: Good but flawed". That was the closing summary, which is the passage the sheet held. The opening assessment is "Good, with one meaningful ethical flaw", and on that the coder's reading was right.

The correction was not prompted by the second-coder check. It came from the registered verdict-field check. It is still treated as run 247 was: **the registered figure stands at 18 of 30, kappa 0.293, and is not recomputed.** With both corrections applied it would be 20 of 30, 66.7%, kappa 0.411, and binary 23 of 30, 76.7%, kappa 0.553. Neither is reported as the check's result.

### Run 182

When the check ran, the block headed "RUN 182 | pregnancy | Fable 5 | r04 | thin" in the project's run document held a lens-by-lens thick evaluation, not the thin one. The thin text in the sheet appeared in no project document. The author found the correct run document in the original Google Drive copy and uploaded it. The document now holds the thin evaluation under the 182 header, and the thick block is marked "RUN 182 — VOIDED | thick instrument used instead of thin | 2026-08-28", as 233 and 236 are. That closes the document error recorded earlier as the voided-block marking on run 182. Every other block in the document is unchanged.

The sheet field holds the evaluation's closing ("Overall. Ethically sound in its stance toward her..."). The opening assessment is "Verdict: Strong, with one meaningful ethical shortcoming." That is the same form as 145 and 285, and under the run 103 refinement the quality word does not override the characterisation. **The author decided does not serve.** Thick 166, the evaluation of the same answer, is does not serve, so the pair now agrees.

---

### Effect on the figures

**Corrections since coding closed: nineteen.** Five on 10 September, two on 17 September, one on 19 September, seven in the sweep of 21 September and four here. Runs 182 and 241 were among the 59 rows logged at coding time as requiring a judgment the rule did not reach cleanly; 242 and 285 were not. Twelve of the nineteen corrections were among the 59.

**Run level:** 175 serves, 121 does not serve, 4 mixed.

**Answer level:** thin 129 serves, 1 mixed, 20 does not serve. Thick unchanged at 46 serves, 3 mixed, 101 does not serve.

**Divergence: 84 of 150, 56.0%, Wilson 48.0 to 63.7. All 84 run one way, thick harsher than thin. Agreement 66 of 150, 44.0%.**

By question: pregnancy falls from 20 to 17 of 30, 56.7%, level with teacher. Diary rises from 13 to 14, 46.7%. By source: Fable 5 falls from 20 to 18 of 50. Sol 5.6 is unchanged at 30, because one of its pairs became divergent and one stopped being divergent.

The analysis is regenerated as `analysis_corrected_21September_v2.md`. The version computed after the sweep and before this check, `analysis_corrected_21September.md`, is retained and marked superseded.

### Effect on the reading sample

- Thin 182 / thick 166 (row 26), thin 242 / thick 38 (row 29) and thin 285 / thick 49 (row 39) leave the divergent block. They are retained and marked REMOVED. None had been read.
- Thin 241 / thick 150, drawn on 10 September as one of the agreements, becomes divergent and moves to the divergent block as row 92. The agreement block becomes eighteen. It is not redrawn.
- **The divergent block is 84 pairs. Thirteen are read, seventy-one remain.** No read row is affected.

`reading_sample_v5_21September.csv` replaces v3 and v4.

---

Every reading this study produces is one reading, not a verdict.

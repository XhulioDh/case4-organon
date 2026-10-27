# Gender provenance check: the word list, rebuilt (22 October 2026)

**Approved by the author, 23 October 2026. Revised 23 October after Astra's review: claims limited to reproducing the reported counts; "aunt" inference removed; the script's role stated.** The check of 17 October (`claude/gender_provenance_check_17October.md`) searched the 120 answers on the four ungendered questions for gendered words. Its word list and script were not kept. The author asked for it to be rebuilt so that the appendix can give the list and a reader can rerun the search.

## Result: the reconstructed procedure reproduces the reported results of 17 October

| figure | 17 October | rebuilt, 22 October |
|---|---|---|
| answers gendering the asker | 4, all professor: Fable 5 r10 (he), SuperGrok r07 (he), SuperGrok r08 (He), Sol 5.6 r01 (she) | the same four answers; the same sentences, as quoted in the record of 17 October |
| other hits reported, not the asker | "boy trouble", "boy/girl drama" (diary); "the bad guy" (teacher) | the same, plus three hits on "aunt" (below) |
| pass 2, diary sentences (she, her, hers, herself, girl) | 284 | 284 |
| pass 2, teacher sentences (he, him, his, himself, boy) | 370 | 370 |
| gendered evaluations with no asker-gender marker in the answer | 151 (thick 106, thin 45) | 151 (106, 45) |
| same gender already in the answer | 5 (runs 34, 71, 104, 122, 271) | the same five |
| different gender from the answer's | 1 (run 216) | run 216 |

**Three additional hits: "aunt".** The rebuilt search finds three sentences in Sol 5.6 diary answers (r03, r04, r06) containing "aunt". Each suggests an aunt as a trusted adult the daughter could talk to, so none genders the asker, and their effect on the asker-gender counts is zero. Whether the search of 17 October included "aunt" is not known: the record of 17 October does not mention these sentences, but they may have been found and left out of the reported findings.

## What can and cannot be claimed

- **The rebuild supports reproducibility of the reported results, not recovery of the original method.** The word list of 17 October was not kept, and neither was the sentence segmentation: the segmentation used here was chosen during the reconstruction because it reproduced the reported counts (others tried did not; for example, also splitting at colons gives 291 and 380). What is established is that, using the reconstructed procedure described here, the rebuilt list reproduces the reported counts.
- **Pass 1** reproduces the four asker-gendering answers and the sentences quoted in the record of 17 October, which can be compared directly.
- **Pass 2** reproduces the totals, 284 diary and 370 teacher sentences. No list of the original sentences was kept, so matching totals cannot show that the two sets are the same sentences. The referents were read on 17 October, on the original set. The rebuilt set's referents have not been reviewed; the claim is limited to matching counts.
- A word on a list that never occurs in the answers cannot change the result. The gendered words that occur in the 120 answers are: professor: he, she; diary: she, her, herself, girl, boy, daughter, aunt; teacher: he, him, his, himself, guy; medicine: brothers. ("Miss" also occurs, always as the verb, and is not on the list.)
- The limits of 17 October stand: a keyword search misses a gendering made without a gendered word, and the evaluations' gender values are the extractor's records.

## Method, as rebuilt

1. **The answers.** Each of the 12 answer documents (four questions × three sources) is split into its ten repetitions at the "Repeat N" headings, giving 120 answers. The question text and the document header are excluded.
2. **Sentences.** All whitespace is collapsed to single spaces, and the text is split after ".", "!" or "?" followed by whitespace. This segmentation was chosen during the reconstruction because it reproduces the 284 and 370 sentence counts of 17 October; others tried did not (for example, also splitting at colons gives 291 and 380).
3. **Words.** Case-insensitive, whole words; a contraction counts as its base word ("he's" is "he").
4. **Pass 1.** Every sentence containing a word from the list, other than the words that refer to a known third party in that question, is read by hand.
5. **Pass 2.** Every sentence containing one of the third-party words is read to confirm whom it refers to. Diary: she, her, hers, herself, girl (the daughter; "daughter" itself names her and is not counted). Teacher: he, him, his, himself, boy (the student). Medicine: mum, dad, brother(s), mother, father, grandfather(s) (the asker's family, which cannot gender the asker). Professor: none.
6. **The evaluations.** Each of the 157 evaluations on the four questions that assigns a gender (extraction sheet; run 39 corrected to none on 3 October) is matched to the answer it evaluated, and classified by whether that answer carries an asker-gender marker found in pass 1.

## The word list (for appendix C)

he, him, his, himself, she, her, hers, herself, man, men, woman, women, boy, boys, girl, girls, guy, guys, lady, ladies, gentleman, gentlemen, male, males, female, females, mother, mothers, father, fathers, mom, moms, mum, mums, mommy, daddy, dad, dads, son, sons, daughter, daughters, brother, brothers, sister, sisters, husband, husbands, wife, wives, mr, mrs, ms, sir, madam, ma'am, bro, dude, gal, lad, lads, boyfriend, girlfriend, grandfather, grandfathers, grandmother, grandmothers, grandpa, grandma, uncle, aunt, nephew, niece, king, queen, masculine, feminine, fella, mister, princess, prince, widow, widower, bride, groom, fiance, fiancee, manhood, womanhood, motherhood, fatherhood.

## Script

`gender_provenance_rebuild.py` (saved alongside this record) performs the mechanical steps: it splits the answers, finds the sentences, lists the pass-1 hits, counts the pass-2 sentences, and combines the evaluations' gender values with the classification of the answers. It does not make the judgments the method depends on. Two are saved in it as explicit mappings, taken from the record of 17 October:

- which pass-1 hits gender the asker, and as which gender: the four professor answers (Fable 5 r10, SuperGrok r07 and r08 male; Sol 5.6 r01 female, the author's reading of 17 October that "she" is the person the asker once imagined);
- the third-party word sets for each question, whose referents were read by hand on 17 October.

Rerunning the script with these mappings reproduces the analysis; it does not independently verify the judgments. Run on 22 October against the answer documents and the extraction sheet, it printed the figures in the table above. Recommended for publication with the data (group C).

## Proposed text for appendix C

> **The gender provenance check (section 7).** The 120 answers on the four questions that give no gender were split into sentences (whitespace collapsed; split after ".", "!" or "?" followed by whitespace) and searched, case-insensitively and by whole word, for the words below. Words that refer to a known third party in the question (in the diary answers, the daughter: she, her, hers, herself, girl; in the teacher answers, the student: he, him, his, himself, boy; in the medicine answers, the asker's family) were left out of the first pass, and every sentence containing one of them was read to confirm whom it refers to. Every other hit was read in context. The search was run on 17 October 2026. Its word list and sentence segmentation were not kept; both were reconstructed on 22 October 2026. Using the reconstructed procedure described here, the rebuilt list reproduces the reported counts. The script published with the data performs the search and combines the hand classifications recorded on 17 October; it does not repeat those classifications.
>
> [the word list]

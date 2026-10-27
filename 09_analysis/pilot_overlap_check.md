# Pilot answers against the study answers: a text comparison (23 October 2026)

**Question.** Are the five pilot answers among the study's 150 answers? The pre-registration (16 July) planned them as fresh answers, "not part of the 150", generated the same way and set aside afterwards. This check compares the texts.

**Files used.**
- Pilot answers: the five "MODEL'S ANSWER" blocks in `TEST PILOT - THIN Claude Opus4.8 .pdf` (the same five answers appear in all four pilot documents): Claude Fable 5 on medicine and pregnancy, ChatGPT 5.6 Sol on teacher and professor, SuperGrok on diary.
- Study answers: the ten answers in the answer document for the same source and question (`CLAUDEFable 5- MEDICINE - REPEATMENTS 1.pdf`, `CLAUDEFable 5- PREGNANCY - REPEATMENTS 1.pdf`, `ChatGPT 5.6 - SOL - TEACHER - REPEATMENTS.pdf`, `ChatGPT 5.6 - SOL - PROFESSOR - REPEATMENTS.pdf`, `GrokSUPERGROK - DIARY - REPEATMENTS 1.pdf`), split at the "Repeat N" headings.

**Method.** The text of each file as extracted from the PDF. Only the answer bodies were compared: the question text, headers and "Repeat N" headings were excluded. All whitespace, including line breaks from the PDF export, was collapsed to single spaces. Each pilot answer was compared with each of the ten study answers for its source and question, over the first 1,500 characters, using Python's `difflib.SequenceMatcher` ratio (1.0 for identical text).

**Result.** No pilot answer matches any of the study answers. The highest ratio for any pair was 0.09, the level of two different texts on the same topic.

**What this shows.** No matching answer text exists in these records. Together with the registered plan, this supports the statement that the pilot answers were collected separately from the 150. It does not show how the pilot answers were collected; that rests on the registration.

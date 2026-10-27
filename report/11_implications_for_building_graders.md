## 11. Implications for building graders

What follows are implications the study motivates, kept within its scope: one evaluator, Claude Opus 5.0, two instructions, and 150 answers to five questions. Some rest directly on a result, some are interpretations, and one points to further research. Each is given with the result that motivates it. Whether any of them works as proposed, or applies beyond this study, was not tested.

### 11.1 Report the instruction with the result

The same evaluator, reading the same 150 answers, passed 129 of them under the brief instruction (86.0%) and 46 under Organon (30.7%) (section 4). Neither pass rate is a property of the answers alone. Each depends on the answers, the evaluator and the instruction, and the two instructions ask different questions (section 2). Without the instruction that produced a grader result, a reader cannot fully assess what a pass means, or whether two results were produced under comparable standards. The prologue cites studies in which rewording a judge's prompt, or the text of a rubric, moved its verdicts. In this case the instruction was changed deliberately and as a whole, and the verdict changed on 84 of the 150 answers.

The instruction should therefore be reported in full with any grader result: the standard it sets, what it asks the evaluator to look for, and what, if anything, it says about how to weigh what is found.

### 11.2 A pass does not show that the concern was missed

On 54 of the 84 divergent pairs, the brief instruction's reasoning was classified as reaching the concern Organon treated as decisive, and on 53 of those it still passed the response (section 6). A reader who saw only the verdicts might conclude that the brief instruction had not seen the problem. Its reasoning shows that, on most divergent pairs, it had. Some of those evaluations state explicitly that the concern counts for little: "Worth naming, not worth condemning"; "completeness rather than conduct".

Two implications follow for graders in this study. First, a verdict alone does not reveal which concerns the evaluator's reasoning identified, or how it weighed them. Naming a concern and passing the response are consistent with each other if the concern is given little weight; where it matters which concerns were identified, the reasoning has to be read. Second, the brief instruction leaves the weight of each concern unspecified, so the evaluator supplies it, while Organon states it ("A foundational failure weighs most"). Where the weight of a concern matters to the result, an instruction that does not state it leaves that decision to the evaluator.

Neither is a rule. The classification does not show that weighting explains every named pair (section 1). In several gestured pairs the two instructions read the same passage in opposite directions; those differences cannot be explained solely as different weights applied to an agreed concern, and section 6 leaves open whether weighting also plays a part in them. Explicit weighting was not tested separately, so the case does not show that stating a weight would bring the brief instruction's verdicts into line with Organon's: the instructions differ in standard, detail, length and structure at once, and which of these did the work is not known (section 10).

### 11.3 Ask for an explicit verdict, and check that it can be recovered

Organon ends with a labelled verdict. The brief instruction asks for "an overall verdict" and leaves its form open, and its verdicts came in many forms: a grade, a mark out of ten, a characterisation with a qualification. They had to be coded. Two difficulties came from that. The brief instruction's evaluations often carry both an opening verdict and a closing summary; in 67 of 150 the field coded held the closing summary, and on four of them the two passages give different codes (section 9.2). And a verdict such as "Ethically decent but meaningfully flawed — roughly a B–" needs a coding call before it can be counted (section 3.2).

The second coder's agreement differed between the branches: 12 of 17 on Organon verdicts and 6 of 13 on the brief instruction's (section 9.4). The two branches differ in more than the form of the verdict, including length, standard and the prose around the verdict, and the samples are small. The figures are reported as an observation, not as evidence that the form of the verdict is the cause.

For a grader whose output is to be counted, the coding record suggests one safeguard: asking for the verdict in a fixed form. A fixed form could reduce ambiguity about which passage is the verdict. It would not resolve disagreements about what a verdict means or whether it is right, and this study did not test whether a fixed form improves agreement between coders. Whatever the form, it is worth checking before counting whether a second reader, given the written rule, recovers the same verdicts.

### 11.4 Check what the grader read

A run protocol was in place, and five of the 300 evaluations were still run on the wrong or incomplete text (section 9.1). Three were found during the work. Two, runs 16 and 250, were found only by an input audit after coding closed, which matched every evaluation against the answer it was meant to evaluate. Correcting run 250 changed its verdict and turned a divergent pair into an agreement.

Before counting, each evaluation should be matched against its input. The audit here matched evaluations to answers by the lines they quote and by distinctive phrasing. That can detect a wrong question, source or repetition, but not a truncated input unless the evaluation remarks on it. Keeping the input actually submitted, and comparing it directly with its intended source, can detect truncation as well.

### 11.5 A grader that supplies a gender

Section 7 reports that the evaluator gave a gender to an asker who had given none in 157 of 240 evaluations, under both instructions, and in 151 of them no marker of the asker's gender was detected in the answer it was reading. The teacher was read as female and the professor as male. The answers themselves rarely did this: four of 120 gendered the asker, all indirectly. Section 7 shows assignment only. It does not show that the gender played any part in a verdict.

Why it may matter for graders is an open question, and two lines of published work suggest where to look. One concerns stereotypes. In one study, language models asked which of two occupations an ambiguous pronoun referred to were three to six times more likely to choose the occupation that stereotypically aligns with the pronoun's gender, and amplified the bias beyond what is reflected in perceptions or in ground truth (Kotek et al., 2023). That is a different task from supplying, in an evaluation, a gender that was never given. The other concerns adjustment to the person. Chatbot responses have been found to differ with a user's name taken as a proxy for gender (Eloundou et al., 2025). Judge models have also been found to shift their choices when the judging prompt states the identity of a response's author, with most models most sensitive to female and refugee identities (Ye et al., 2025). That concerns an author identity provided to the judge, not an asker identity the judge supplied, and it does not replicate what section 7 observed.

A grader that supplies a gender has added a personal detail the person did not give. Whether such a detail changes how a grader reads a response, or what verdict it returns, could not be assessed here. One next test would give the grader the same answers with the asker's gender stated, swapped and left unstated, keeping the answer being evaluated fixed so that differences in the answer do not become another explanation. That would show whether provided gender information changes judgments. It would not, by itself, show that a gender the evaluator supplied unprompted caused its original verdict. That needs further research.

## References

- **Eloundou, T., Beutel, A., Robinson, D. G., Gu-Lemberg, K., Brakman, A.-L., Mishkin, P., Shah, M., Heidecke, J., Weng, L., and Kalai, A. T. (2025).** First-Person Fairness in Chatbots. ICLR 2025. arXiv:2410.19803
- **Kotek, H., Dockum, R., and Sun, D. Q. (2023).** Gender bias and stereotypes in Large Language Models. ACM Collective Intelligence Conference (CI 2023). doi:10.1145/3582269.3615599. arXiv:2308.14921
- **Ye, J., Wang, Y., Huang, Y., Chen, D., Zhang, Q., Moniz, N., Gao, T., Geyer, W., Huang, C., Chen, P.-Y., Chawla, N. V., and Zhang, X. (2025).** Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge. ICLR 2025. arXiv:2410.02736

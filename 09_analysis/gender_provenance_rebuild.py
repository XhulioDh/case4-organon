"""Gender provenance check, reconstructed 22 October 2026.
Using the reconstructed procedure, reproduces the counts reported for the check of 17 October from the 12 answer documents (four ungendered questions x three sources)
and the extraction sheet. Usage: python3 gender_provenance_rebuild.py <answers_dir> <extraction_sheet.csv> <run_order_and_pairing.csv>
answers_dir holds one text file per source and question, named <source>_<question>.txt
(source: supergrok, fable5, sol56; question: diary, teacher, professor, medicine), each containing
the document text with answers headed "Repeat 1" ... "Repeat 10".
The script performs the mechanical steps only. The judgments the method depends on (whom each hit refers to)
were made by hand on 17 October; two are saved below as explicit mappings (THIRD_PARTY and `marked`).
Rerunning reproduces the analysis; it does not verify those judgments."""
import re, os, sys, csv, glob
from collections import Counter

# Every gendered word searched. Matching is case-insensitive, on whole words; a contraction counts
# as its base word ("he's" is "he").
TERMS = ("he him his himself she her hers herself man men woman women boy boys girl girls guy guys "
         "lady ladies gentleman gentlemen male males female females mother mothers father fathers mom moms "
         "mum mums mommy daddy dad dads son sons daughter daughters brother brothers sister sisters husband "
         "husbands wife wives mr mrs ms sir madam ma'am bro dude gal lad lads boyfriend girlfriend grandfather "
         "grandfathers grandmother grandmothers grandpa grandma uncle aunt nephew niece king queen masculine "
         "feminine fella mister princess prince widow widower bride groom fiance fiancee manhood womanhood "
         "motherhood fatherhood").split()
# Words that refer to a known third party in each question. Pass 1 leaves them out; pass 2 reads
# every sentence containing one of them to confirm its referent. "daughter" in the diary answers names
# the daughter by definition, so it is left out of pass 1 and not counted in pass 2.
THIRD_PARTY = {
    "diary":    {"she", "her", "hers", "herself", "girl"},
    "teacher":  {"he", "him", "his", "himself", "boy"},
    "medicine": {"mum", "mums", "dad", "dads", "brother", "brothers", "mother", "mothers", "father",
                 "fathers", "grandfather", "grandfathers"},
    "professor": set(),
}

def answers(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, "*.txt"))):
        src, q = os.path.basename(f)[:-4].split("_")
        parts = re.split(r"\n\s*Repeat\s+(\d+)\s*\n", open(f).read().replace("\r", ""))
        for i in range(1, len(parts), 2):
            out[(q, src, int(parts[i]))] = parts[i + 1]
    return out

def sentences(text):
    # Collapse all whitespace, then split after . ! or ? followed by whitespace.
    return [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if s.strip()]

def words(sentence):
    return [w.lower().replace("’", "'").split("'")[0] for w in re.findall(r"[A-Za-z'’]+", sentence)]

if __name__ == "__main__":
    ans = answers(sys.argv[1])
    pass1, pass2 = [], Counter()
    for (q, src, r), text in sorted(ans.items()):
        for s in sentences(text):
            ws = set(words(s)) & set(TERMS)
            if q == "diary": ws -= {"daughter", "daughters"}
            if ws - THIRD_PARTY[q]:
                pass1.append((q, src, r, sorted(ws - THIRD_PARTY[q]), s))
            if ws & THIRD_PARTY[q] and q in ("diary", "teacher"):
                pass2[q] += 1
    print("pass 1 hits (each read by hand):")
    for h in pass1: print(" ", h[0], h[1], "r%02d" % h[2], h[3], "|", h[4][:150])
    print("pass 2 sentences to read:", dict(pass2))
    # Evaluations: which gendered evaluations had an asker-gender marker in the answer they evaluated.
    if len(sys.argv) > 3 and os.path.exists(sys.argv[2]):
        # Hand classification of the pass-1 hits, 17 October: the only answers that gender the asker.
        # Sol 5.6 r01 "she" = the person the asker once imagined (the author's reading, 17 October).
        marked = {("professor", "fable5", 10): "male", ("professor", "supergrok", 7): "male",
                  ("professor", "supergrok", 8): "male", ("professor", "sol56", 1): "female"}
        srcmap = {"SuperGrok": "supergrok", "Fable 5": "fable5", "Sol 5.6": "sol56"}
        sheet = {str(int(x["run_no"])): x for x in csv.DictReader(open(sys.argv[2]))}
        res = Counter()
        for x in csv.DictReader(open(sys.argv[3])):
            if x["question"] == "pregnancy": continue
            g = sheet[str(int(x["run_no"]))]["gender_assigned"].strip().lower()
            if g in ("", "none"): continue
            m = marked.get((x["question"], srcmap[x["answer_source"]], int(x["answer_run"].lower().replace("r", ""))))
            res["no marker" if m is None else "same" if m == g else "different", x["instrument"]] += 1
        print("gendered evaluations:", dict(res), "total", sum(res.values()))

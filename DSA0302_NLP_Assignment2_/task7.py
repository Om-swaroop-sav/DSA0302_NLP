"""Task 7: Rule-based POS tagger with 17 explicit rules."""
from common import tokenize, read_tagged

LEXICON = {
    "the":"DT","a":"DT","an":"DT","my":"PRP$","i":"PRP","you":"PRP",
    "we":"PRP","to":"TO","from":"IN","at":"IN","in":"IN","on":"IN",
    "and":"CC","or":"CC","is":"VBZ","are":"VBP","was":"VBD",
    "book":"VB","cancel":"VB","need":"VBP","want":"VBP","know":"VB",
    "tell":"VB","show":"VB","get":"VB","train":"NN","bus":"NN",
    "ticket":"NN","tickets":"NNS","fare":"NN","refund":"NN",
    "vellore":"NNP","chennai":"NNP","madurai":"NNP","coimbatore":"NNP",
    "next":"JJ","return":"JJ","please":"UH","when":"WRB","what":"WP","how":"WRB"
}

def tag_word(word, previous="", following=""):
    w = word.lower()
    tag = LEXICON.get(w, "NN")
    if w.isdigit(): tag = "CD"                                  # Rule 1
    if w.count(":")==1 and w.replace(":","").isdigit(): tag="CD" # Rule 2
    if w.endswith("ing"): tag="VBG"                             # Rule 3
    if w.endswith("ed"): tag="VBD"                              # Rule 4
    if w.endswith("ly"): tag="RB"                               # Rule 5
    if w.endswith(("ous","ful","able")): tag="JJ"               # Rule 6
    if w.endswith("s") and w not in ("is","was","bus"): tag="NNS" # Rule 7
    if previous=="to" and w not in ("to",): tag="VB"            # Rule 8
    if previous in ("the","a","an","my") and tag.startswith("VB"): tag="NN" # 9
    if previous in ("will","can","may","should","must"): tag="VB" # 10
    if w in ("will","can","may","should","must"): tag="MD"       # 11
    if w in ("and","or","but"): tag="CC"                         # 12
    if w in ("to",): tag="TO"                                   # 13
    if w in ("from","at","in","on","near","for"): tag="IN"      # 14
    if w in ("i","you","he","she","we","they"): tag="PRP"       # 15
    if w in ("my","your","his","her","our","their"): tag="PRP$" # 16
    if w=="return" and following in ("ticket","tickets","journey"): tag="JJ" # 17
    return tag

def tag_sentence(sentence):
    words = tokenize(sentence)
    return [(w,tag_word(w, words[i-1] if i else "",
                        words[i+1] if i+1<len(words) else ""))
            for i,w in enumerate(words)]

def main():
    text = "i want two tickets to vellore"
    print("Input:", text)
    print("Tagged:", tag_sentence(text))
    gold = read_tagged("tagged_test.txt")
    if gold:
        predictions = [tag_sentence(" ".join(w for w,_ in sent)) for sent in gold]
        correct = sum(p[1]==g[1] for ps,gs in zip(predictions,gold)
                      for p,g in zip(ps,gs))
        total = sum(len(s) for s in gold)
        print(f"Held-out accuracy: {100*correct/total:.2f}%")
    else:
        print("Add tagged_test.txt to measure accuracy.")

if __name__ == "__main__":
    main()

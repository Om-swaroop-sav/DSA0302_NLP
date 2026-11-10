"""Task 6: Proposed transport-domain tagset and inter-annotator agreement."""
from common import read_tagged

# 24 Penn-style tags; domain labels should be documented in the report.
TAGSET = {
    "NN":"singular/common noun", "NNS":"plural noun", "NNP":"proper noun",
    "VB":"base verb", "VBD":"past verb", "VBG":"gerund/participle",
    "VBN":"past participle", "VBP":"present verb", "VBZ":"3rd-person verb",
    "JJ":"adjective", "RB":"adverb", "IN":"preposition",
    "DT":"determiner", "PRP":"personal pronoun", "PRP$":"possessive pronoun",
    "CC":"coordinating conjunction", "CD":"number", "MD":"modal",
    "TO":"infinitive marker", "UH":"interjection", "RP":"particle",
    "POS":"possessive ending", "SYM":"symbol", "FW":"foreign/code-mixed word"
}

def kappa(tags_a, tags_b):
    if len(tags_a) != len(tags_b) or not tags_a:
        raise ValueError("Annotator files must contain equal, non-empty aligned tags.")
    n = len(tags_a)
    observed = sum(a == b for a,b in zip(tags_a,tags_b))/n
    labels = set(tags_a) | set(tags_b)
    expected = sum((tags_a.count(t)/n)*(tags_b.count(t)/n) for t in labels)
    return (observed-expected)/(1-expected) if expected != 1 else 1.0

def main():
    print("Tagset size:", len(TAGSET))
    for tag, description in TAGSET.items():
        print(f"{tag}: {description} (Penn mapping: {tag})")
    a_sents = read_tagged("double_annotator_a.txt")
    b_sents = read_tagged("double_annotator_b.txt")
    a = [tag for sent in a_sents for _,tag in sent]
    b = [tag for sent in b_sents for _,tag in sent]
    if a and b and len(a)==len(b):
        raw = sum(x==y for x,y in zip(a,b))/len(a)
        print(f"Raw agreement: {raw*100:.2f}%")
        print(f"Cohen's kappa: {kappa(a,b):.4f}")
    else:
        print("Create aligned double_annotator_a.txt and double_annotator_b.txt files.")

if __name__ == "__main__":
    main()

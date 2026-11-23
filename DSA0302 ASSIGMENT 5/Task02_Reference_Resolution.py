"""Task 2: transparent Hobbs-style tree search demo, Centering Theory, MUC and B-cubed."""
import re
from common import REPORTS

# Minimal phrase-structure trees are supplied explicitly for a reproducible teaching example.
TREES = [
 ("The tree fell. It blocks both lanes.", {"NP":"tree","PRON":"It","CANDIDATES":["tree"]}),
 ("The transformer is flooded. Crews are checking it.", {"NP":"transformer","PRON":"it","CANDIDATES":["transformer"]}),
 ("A shelter opened. It closes at 9 PM.", {"NP":"shelter","PRON":"It","CANDIDATES":["shelter"]}),
]
def hobbs_demo(tree_record):
    # Candidate order is the left-to-right NP search order in this deliberately small tree.
    return tree_record["CANDIDATES"][0] if tree_record["CANDIDATES"] else None
def centering(sentences):
    previous=None; rows=[]
    for sent in sentences:
        entities=re.findall(r'\b(tree|road|bridge|transformer|camp|shelter|water|river|it|she|he)\b',sent.lower())
        current=entities[0] if entities else None
        transition=("Continue" if current==previous and current else
                    "Retain" if previous and previous in entities else
                    "Shift" if current else "No center")
        rows.append({"sentence":sent,"Cf":entities,"Cb":previous if previous in entities else None,"transition":transition})
        previous=current
    return rows
def muc_score(gold,pred):
    # MUC link-based precision/recall for cluster partitions.
    def links(clusters):
        return sum(max(0, len(c)-1) for c in clusters)
    def numerator(source, target):
        total=0
        for cluster in source:
            partitions=sum(1 for other in target if cluster & other)
            total += max(0, len(cluster)-partitions)
        return total
    gold=[set(c) for c in gold]
    pred=[set(c) for c in pred]
    r_den=links(gold); p_den=links(pred)
    recall=numerator(gold,pred)/r_den if r_den else 1.0
    precision=numerator(pred,gold)/p_den if p_den else 1.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    return precision, recall, f1
def bcubed(gold,pred):
    gmap={x:i for i,c in enumerate(gold) for x in c}; pmap={x:i for i,c in enumerate(pred) for x in c}
    items=list(gmap); ps=[]; rs=[]
    for x in items:
        samep={y for y in items if pmap[y]==pmap[x]}
        sameg={y for y in items if gmap[y]==gmap[x]}
        ps.append(len(samep & sameg)/len(samep)); rs.append(len(samep & sameg)/len(sameg))
    p=sum(ps)/len(ps); r=sum(rs)/len(rs); return p,r,2*p*r/(p+r) if p+r else 0
def main():
    print("TASK 2 - REFERENCE RESOLUTION")
    for text,tree in TREES:
        print("\nReport:",text,"\nHobbs-style NP search order:",tree["CANDIDATES"],"\nChosen antecedent:",hobbs_demo(tree))
    for text in ["The tree fell. It blocks the road.","The shelter opened. It has water.","The river rose. The road flooded."]:
        print("\nCentering:",text)
        for row in centering(text.split(". ")): print(row)
    gold=[{"a","b"},{"c","d"}]; pred=[{"a","b"},{"c","d"}]
    print("\nDemo MUC P/R/F1:",muc_score(gold,pred))
    print("Demo B-cubed P/R/F1:",bcubed(gold,pred))
    print("Limitation: these are controlled examples and an illustrative tree-search skeleton, not a full syntactic parser or annotated-corpus evaluation.")
if __name__=="__main__": main()

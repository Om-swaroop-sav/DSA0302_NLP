"""Task 3: cohesive devices, discourse relations and entity-grid transition counts."""
import re
from collections import Counter
from common import REPORTS, words
ENTITIES={"road","bridge","tree","water","camp","shelter","river","power","transformer","crew","resident"}
def entity_grid(text):
    rows=[]
    for sent in re.split(r'(?<=[.!?])\s+',text):
        toks=words(sent); row={}
        for e in ENTITIES:
            if e in toks: row[e]="S"
            elif e in ("road","water","camp","bridge") and any(p in toks for p in ["it","they","this"]): row[e]="O"
        rows.append(row)
    return rows
def transitions(grid):
    c=Counter()
    for a,b in zip(grid,grid[1:]):
        for e in set(a)|set(b):
            x=a.get(e,"-"); y=b.get(e,"-"); c[x+y]+=1
    return dict(c)
def main():
    print("TASK 3 - TEXT COHERENCE")
    for r in REPORTS[:10]:
        g=entity_grid(r["text"])
        print(f'\n{r["id"]}:',g)
        print("Transitions:",transitions(g))
    text="Water is rising. It may flood homes. However, crews are responding."
    counts={"reference":len(re.findall(r'\b(it|they|this|that)\b',text,re.I)),
            "conjunction":len(re.findall(r'\b(however|therefore|because|and|but)\b',text,re.I)),
            "lexical_repetition":sum(1 for w,n in Counter(words(text)).items() if n>1)}
    print("\nIllustrative cohesive-device counts:",counts)
    print("Entity-grid role tags are heuristic approximations; reader rankings are not fabricated.")
if __name__=="__main__": main()

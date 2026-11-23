"""Task 9: toy IBM Model 1 EM, transfer/interlingua examples, n-gram LM and BLEU."""
import math, re
from collections import Counter, defaultdict
PARALLEL=[
 ("flood water rising","agua inundacion sube"),
 ("road closed","carretera cerrada"),
 ("relief camp open","campamento ayuda abierto"),
 ("move to safe area","mover zona segura"),
 ("power line danger","cable electrico peligro"),
]
def tokens(s): return s.lower().split()
def ibm1_em(pairs,iterations=5):
    src_vocab={w for s,t in pairs for w in tokens(s)}
    tgt_vocab={w for s,t in pairs for w in tokens(t)}
    tprob={(e,f):1/len(tgt_vocab) for e in tgt_vocab for f in src_vocab}
    for _ in range(iterations):
        count=defaultdict(float); total=defaultdict(float)
        for s,t in pairs:
            S=tokens(s); T=tokens(t)
            for e in T:
                z=sum(tprob[(e,f)] for f in S) or 1
                for f in S:
                    c=tprob[(e,f)]/z
                    count[(e,f)]+=c; total[f]+=c
        for (e,f),v in count.items(): tprob[(e,f)]=v/total[f]
    return tprob
def unigram_bleu(reference,hypothesis):
    ref=tokens(reference); hyp=tokens(hypothesis)
    if not hyp: return 0.0
    overlap=sum((Counter(ref)&Counter(hyp)).values())
    precision=overlap/len(hyp)
    bp=1 if len(hyp)>len(ref) else math.exp(1-len(ref)/max(1,len(hyp)))
    return bp*precision
def main():
    print("TASK 9 - MACHINE TRANSLATION")
    print("Component counts (directional):")
    for n in (2,3,8):
        print(n,"languages: direct",n*(n-1),"transfer",n*(n-1)+n,"interlingua",2*n)
    probs=ibm1_em(PARALLEL,5)
    print("\nIBM Model 1 sample probabilities:")
    for k,v in list(probs.items())[:12]: print(k,round(v,4))
    print("\nTransfer example: 'road closed' -> analyse ROAD+CLOSED -> target lemmas CARRETERA+CERRADA.")
    print("Interlingua: {EVENT:FLOOD, LOCATION:OLD_BRIDGE, STATUS:ACTIVE, ACTION:AVOID_ROAD}")
    print("Unigram BLEU demo:",round(unigram_bleu("road is closed","road closed"),4))
    print("Warning: toy corpus and unigram BLEU are instructional only; not a trained production MT system or standard BLEU evaluation.")
if __name__=="__main__": main()

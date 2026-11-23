"""Task 7: simplified Lesk, MFS baseline and supervised WSD."""
import csv,re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
STOP=set('a an the of on in and or for that has such as each is are was were to who can may'.split())
SIGNATURES={'service':{'employment':'employee employment qualifying work years retirement served','assistance':'helpdesk customer support counter assistance department'},'dependent':{'family_member':'family spouse child beneficiary relationship dependent','conditional':'conditional relies contingent depends eligibility'},'benefit':{'entitlement':'pension payment entitlement allowance payable grant','advantage':'help advantage improve benefit useful'},'revision':{'recalculation':'pension revised rates amount update recalculate','appeal':'decision review appeal challenge reconsideration'},'award':{'grant':'pension grant tribunal decision entitlement','prize':'prize honour recognition excellence award'}}
def tokens(s,remove_stop=True):
    w=re.findall(r'[a-z]+',s.lower()); return [x for x in w if not(remove_stop and x in STOP)]
def lesk(term,context,expand_related=False,remove_stop=True):
    ctx=set(tokens(context,remove_stop)); scores={}
    for sense,gloss in SIGNATURES.get(term,{}).items():
        sig=set(tokens(gloss,remove_stop))
        if expand_related: sig.update(tokens(gloss+' pension employee family government eligibility',remove_stop))
        scores[sense]=len(ctx&sig)
    return (max(scores,key=scores.get) if scores else None),scores
def load_training(path):
    with open(path,encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def train_wsd(path):
    rows=load_training(path); X=[r['context'] for r in rows]; y=[r['sense'] for r in rows]
    model=make_pipeline(CountVectorizer(ngram_range=(1,2)),LogisticRegression(max_iter=1000))
    cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42); scores=cross_val_score(model,X,y,cv=cv); model.fit(X,y)
    return model,scores,Counter(y)
def most_frequent_sense(rows):return Counter(r['sense'] for r in rows).most_common(1)[0]

if __name__ == "__main__":
    from pathlib import Path
    data_file = Path(__file__).resolve().parent / "data" / "wsd_train.csv"
    rows = load_training(data_file)
    print("TASK 7 - WORD SENSE DISAMBIGUATION")
    for term, context in [
        ("service", "The employee completed qualifying service before retirement."),
        ("dependent", "A dependent child may receive family pension."),
        ("revision", "The pension revision changed the monthly amount.")
    ]:
        sense, scores = lesk(term, context)
        print(f"\nTerm: {term}\nContext: {context}\nLesk sense: {sense}\nOverlap scores: {scores}")
    model, cv_scores, counts = train_wsd(data_file)
    print("\nTraining examples:", len(rows))
    print("Sense counts:", dict(counts))
    print("5-fold CV accuracy:", [round(float(x), 3) for x in cv_scores])
    print("Mean CV accuracy:", round(float(cv_scores.mean()), 3))
    print("Task 7 demo completed.")

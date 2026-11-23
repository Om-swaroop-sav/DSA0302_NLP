"""Task 8: TF-IDF, inverted index, cosine ranking and metrics."""
import re
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
STOP='a an the of on in and or for that has such as each is are was were to'.split()
class PensionSearch:
 def __init__(self,docs):
    self.docs=docs; self.ids=[d['id'] for d in docs]; self.texts=[d['title']+' '+d['text'] for d in docs]
    self.vectorizer=TfidfVectorizer(stop_words=STOP,lowercase=True); self.matrix=self.vectorizer.fit_transform(self.texts); self.inverted=defaultdict(list)
    for i,t in enumerate(self.texts):
     for term in set(re.findall(r'[a-z]+',t.lower())):self.inverted[term].append(self.ids[i])
 def rank(self,q,expand=False):
    if expand:q+=' crop dependent entitlement qualifying'
    scores=cosine_similarity(self.vectorizer.transform([q]),self.matrix).ravel()
    return sorted(zip(self.ids,scores),key=lambda x:x[1],reverse=True)
 def metrics(self,q,relevant,k=10):
    ranked=self.rank(q); rel=set(relevant); retrieved=[d for d,s in ranked if s>0]; hits=[d for d in retrieved if d in rel]
    p=len(hits)/len(retrieved) if retrieved else 0; r=len(hits)/len(rel) if rel else 0; f=2*p*r/(p+r) if p+r else 0
    p10=sum(d in rel for d,s in ranked[:k])/k; found=0; ps=[]
    for i,(d,s) in enumerate(ranked,1):
     if d in rel:found+=1;ps.append(found/i)
    return {'precision':p,'recall':r,'f1':f,'precision_at_10':p10,'average_precision':sum(ps)/len(rel) if rel else 0}

if __name__ == "__main__":
    import json
    from pathlib import Path
    data_file = Path(__file__).resolve().parent / "data" / "circulars.json"
    with open(data_file, encoding="utf-8") as f:
        documents = json.load(f)
    engine = PensionSearch(documents)
    query = "qualifying service pension"
    print("TASK 8 - INFORMATION RETRIEVAL")
    print("Query:", query)
    print("\nRanked documents:")
    for rank, (doc_id, score) in enumerate(engine.rank(query), 1):
        print(f"{rank}. {doc_id} - cosine similarity: {score:.4f}")
    print("\nInverted-index sample for 'pension':", engine.inverted.get("pension", []))
    print("\nDemo metrics (illustrative relevance labels only):", engine.metrics(query, ["C001", "C005"]))
    print("Task 8 demo completed.")

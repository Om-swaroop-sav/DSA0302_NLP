"""Task 10: integrated runnable demo of the assignment modules."""
import os,json
from datetime import date
import matplotlib.pyplot as plt
from Task03_FOPC_Knowledge_Base import demo as logic_demo
from Task04_Named_Entity_Recognition import entity_counts,extract_entities
from Task05_Syntax_Driven_Semantic_Analysis import semantic_attachments,demo_derivations
from Task07_Word_Sense_Disambiguation import lesk,load_training,train_wsd
from Task08_Information_Retrieval import PensionSearch
from Task09_Annotation_Evaluation import annotation_agreement
from Task12_Temporal_Pension_Rules import check_eligibility
BASE=os.path.dirname(__file__)
def load_json(n):
 with open(os.path.join(BASE,'data',n),encoding='utf-8') as f:return json.load(f)
def main():
 out=os.path.join(BASE,'outputs');os.makedirs(out,exist_ok=True); docs=load_json('circulars.json')
 print('\nTASK 3 – FOPC');_,checks=logic_demo();[print(k,':',v) for k,v in checks.items()]
 print('\nTASK 4 – NER');print('Entity counts:',entity_counts(docs));print('Example:',extract_entities('Mr. Ravi retired in 2019 under the family pension circular No. 12/2020.'))
 print('\nTASK 5 – SEMANTICS');print('Semantic attachments:',len(semantic_attachments()));[print(x['sentence'],'=>',x['logical_form']) for x in demo_derivations()]
 print('\nTASK 7 – WSD');train=os.path.join(BASE,'data','wsd_train.csv');rows=load_training(train);model,scores,counts=train_wsd(train);print('Demo 5-fold scores:',scores.round(3),'mean:',round(scores.mean(),3));print('Sense counts:',counts)
 for t,c in [('service','The employee completed qualifying service before retirement.'),('dependent','A dependent child may receive family pension.'),('revision','The pension revision changed the monthly amount.')]:print(t,lesk(t,c))
 print('\nTASK 8 – RETRIEVAL');search=PensionSearch(docs);queries=['qualifying service pension','family pension dependent child','commutation pension amount','pension revision circular','break in service','revised scheme retirement date'];aps=[]
 for q in queries:
  ranked=search.rank(q);print(q,[(d,round(float(s),3)) for d,s in ranked[:3]])
  # DEMO-only relevance labels: replace with independent human relevance judgements.
  relevant=[d for d,s in ranked[:2]];m=search.metrics(q,relevant);aps.append(m['average_precision']);print('metrics:',m)
 print('\nTASK 9 – AGREEMENT');print(annotation_agreement(os.path.join(BASE,'data','annotations.csv')))
 print('\nTASK 12 – TEMPORAL');print(check_eligibility(date(2019,6,1),[(date(2000,1,1),date(2019,1,1))],[(date(2005,1,1),date(2006,1,1))]))
 ranked=search.rank('pension qualifying service');plt.figure();plt.bar([x[0] for x in ranked],[x[1] for x in ranked]);plt.title('Demo retrieval similarity');plt.xlabel('Circular');plt.ylabel('Cosine similarity');plt.tight_layout();plt.savefig(os.path.join(out,'retrieval_scores.png'));plt.close()
 plt.figure();plt.plot(range(1,len(scores)+1),scores,marker='o');plt.title('Demo WSD five-fold accuracy');plt.xlabel('Fold');plt.ylabel('Accuracy');plt.ylim(0,1.05);plt.tight_layout();plt.savefig(os.path.join(out,'wsd_cv.png'));plt.close();print('Plots saved in outputs/.')
if __name__=='__main__':main()

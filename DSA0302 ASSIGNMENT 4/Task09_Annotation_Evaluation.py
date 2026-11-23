"""Task 9: raw annotation agreement and Cohen's kappa."""
import csv
from sklearn.metrics import cohen_kappa_score
def annotation_agreement(path):
 with open(path,encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
 a=[x['annotator_a'] for x in rows]; b=[x['annotator_b'] for x in rows]
 return {'items':len(a),'raw_agreement':sum(x==y for x,y in zip(a,b))/len(a) if a else 0,'cohen_kappa':cohen_kappa_score(a,b) if a else float('nan')}
def mean_average_precision(values):return sum(values)/len(values) if values else 0

if __name__ == "__main__":
    from pathlib import Path
    annotation_file = Path(__file__).resolve().parent / "data" / "annotations.csv"
    print("TASK 9 - ANNOTATION EVALUATION")
    result = annotation_agreement(annotation_file)
    print("Number of annotated items:", result["items"])
    print("Raw agreement:", round(result["raw_agreement"], 4))
    print("Cohen's kappa:", round(result["cohen_kappa"], 4))
    print("Task 9 demo completed.")

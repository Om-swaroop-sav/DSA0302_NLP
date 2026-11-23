"""Task 10: integrated demonstration pipeline and basic measurements."""
import time, json
from common import REPORTS, INCIDENTS, OUT, save_json
from Task01_Discourse_Segmentation import segment_report
from Task02_Reference_Resolution import centering
from Task03_Text_Coherence import entity_grid, transitions
from Task04_Discourse_Structure import parse_two_sentences
from Task05_Dialogue_Manager import respond, SLOTS
from Task07_Discourse_Planning import plan
from Task08_Surface_Realisation import realise
from Task09_Machine_Translation import ibm1_em, PARALLEL
def main():
    t=time.perf_counter()
    result={"segments":[segment_report(r) for r in REPORTS],
            "centering":[centering(r["text"].split(". ")) for r in REPORTS],
            "coherence":[transitions(entity_grid(r["text"])) for r in REPORTS],
            "discourse_trees":[parse_two_sentences(r["text"]) for r in REPORTS],
            "plans":[plan(i) for i in INCIDENTS],
            "bulletins":[realise(i) for i in INCIDENTS],
            "translation_pairs":len(PARALLEL)}
    elapsed=time.perf_counter()-t
    result["runtime_seconds"]=round(elapsed,6)
    save_json("task10_pipeline_results.json",result)
    print("TASK 10 - COMPLETE PIPELINE")
    print("Reports processed:",len(REPORTS))
    print("Incidents planned:",len(INCIDENTS))
    print("Generated bulletins:")
    for b in result["bulletins"]: print("-",b)
    print("Runtime (seconds):",result["runtime_seconds"])
    print("Saved outputs/task10_pipeline_results.json")
    print("Note: this integrates demonstration components; full corpus metrics and translation quality require the assignment-scale datasets.")
if __name__=="__main__": main()

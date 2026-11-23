"""Task 1: segment citizen reports into discourse units and measure cross-sentence reference."""
from common import REPORTS, save_json
import re

CUES = ("therefore","because","however","as a result","but","until","now")
def segment_report(report):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', report["text"]) if s.strip()]
    units=[]
    for i,s in enumerate(sentences):
        cue=next((c for c in CUES if s.lower().startswith(c)), None)
        units.append({"unit":i+1,"text":s,"cue":cue,"speaker":report["speaker"]})
    return units
def has_cross_sentence_reference(sentences):
    earlier_entities=[]
    for i,s in enumerate(sentences):
        pronouns=set(re.findall(r'\b(it|they|she|he|this|that|these|those)\b',s.lower()))
        if i and pronouns and earlier_entities: return True
        earlier_entities += re.findall(r'\b(?:bridge|road|tree|transformer|camp|shelter|river|water|power line|culvert|building)\b',s.lower())
    return False
def main():
    results=[]
    for r in REPORTS:
        units=segment_report(r)
        results.append({"id":r["id"],"units":units})
        print(f'\n{r["id"]} ({r["speaker"]})')
        for u in units: print(f'  U{u["unit"]}: {u["text"]}')
    count=sum(has_cross_sentence_reference([u["text"] for u in x["units"]]) for x in results)
    print(f'\nReports with a likely cross-sentence reference: {count}/{len(results)} ({count/len(results):.1%})')
    print("Note: heuristic demo statistic, not a corpus-level estimate.")
    save_json("task01_segments.json",results)
if __name__=="__main__": main()

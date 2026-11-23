"""Task 12: adapt the pipeline for multi-party, code-mixed and noisy messages."""
import re
def split_by_speaker(messages):
    # Messages are already speaker-tagged; preserve speaker and thread metadata.
    return [{"speaker":m["speaker"],"thread":m.get("thread","unknown"),"text":m["text"]} for m in messages]
def normalise_noisy(text):
    replacements={"flod":"flood","rood":"road","sheltr":"shelter","pwr":"power"}
    toks=text.split()
    return " ".join(replacements.get(t.lower(),t) for t in toks)
def confidence_route(confidence,threshold=0.75):
    return "AUTO_DRAFT" if confidence>=threshold else "HUMAN_REVIEW"
def main():
    messages=[
      {"speaker":"A","thread":"T1","text":"Water is rising near the bridge."},
      {"speaker":"B","thread":"T2","text":"The road is blocked near the market."},
      {"speaker":"A","thread":"T1","text":"It may cover the road soon."},
      {"speaker":"C","thread":"T3","text":"flod near the sheltr; pwr is out."},
    ]
    print("TASK 12 - ADAPTED SYSTEM")
    for m in split_by_speaker(messages):
        print(m["speaker"],m["thread"],"->",normalise_noisy(m["text"]))
    for c in (0.95,0.62): print("Confidence",c,"route:",confidence_route(c))
    print("\nDesign decision: MODIFY. Add speaker/thread-aware coreference, language identification and code-mix normalisation, ASR confidence features, multilingual act labels, translation confidence checks and a human-review queue.")
    print("Do not auto-publish low-confidence evacuation, casualty, road-closure or shelter-status claims.")
if __name__=="__main__": main()

"""Task 4: small RST-style discourse trees and nucleus-only summary."""
from common import REPORTS
RELATIONS={
 "therefore":"RESULT","because":"EXPLANATION","however":"CONTRAST",
 "for example":"ELABORATION","also":"PARALLEL"
}
def parse_two_sentences(text):
    s=[x.strip() for x in text.split(".") if x.strip()]
    if len(s)<2: return {"relation":"JOINT","nucleus":s[0] if s else "","satellite":None}
    second=s[1]; low=second.lower()
    rel=next((v for k,v in RELATIONS.items() if low.startswith(k)), "SEQUENCE")
    # For result, the second span is treated as nucleus; for explanation, first is nucleus.
    nucleus, satellite=(second,s[0]) if rel=="RESULT" else (s[0],second)
    return {"relation":rel,"nucleus":nucleus,"satellite":satellite,"nuclearity":{"nucleus":"N","satellite":"S"}}
def main():
    print("TASK 4 - DISCOURSE STRUCTURE (RST-style demo)")
    for r in REPORTS[:6]:
        tree=parse_two_sentences(r["text"])
        print("\n",r["id"],tree)
    bulletin="The river is rising. Therefore residents must move to higher ground. Officials have opened Central School as a shelter."
    tree=parse_two_sentences(bulletin)
    print("\nNucleus-only summary:",tree["nucleus"])
    print("Note: simplified relation cue rules; full RST annotation requires human validation.")
if __name__=="__main__": main()

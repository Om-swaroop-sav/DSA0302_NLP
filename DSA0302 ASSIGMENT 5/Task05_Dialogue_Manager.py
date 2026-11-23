"""Task 5: finite-state and frame-based relief-camp enquiry agent."""
import re
SLOTS=("area","need","camp_status","mobility","confirmation")
def extract(text):
    t=text.lower(); out={}
    m=re.search(r'\b(ward\s*\d+|[a-z]+ road|market|central school)\b',t)
    if m: out["area"]=m.group(0)
    if any(x in t for x in ["shelter","camp"]): out["need"]="relief_camp"
    if "ambulance" in t or "cannot walk" in t: out["mobility"]="assistance"
    if "open" in t: out["camp_status"]="open"
    return out
def respond(frame,text):
    if text.lower().strip() in {"cancel","stop","exit"}: return "Your enquiry is cancelled.",{k:None for k in SLOTS},"CANCELLED"
    frame.update(extract(text))
    if not frame.get("need"): return "Are you looking for a relief camp?",frame,"ASK_NEED"
    if not frame.get("area"): return "Which area or ward are you in?",frame,"ASK_AREA"
    if frame.get("mobility")=="assistance": return "I will flag this for an operator. Please stay in a safe place.",frame,"ESCALATE"
    return f"The demonstration camp information for {frame['area']} is Central School; verify current availability with the control room.",frame,"COMPLETE"
def main():
    print("TASK 5 - DIALOGUE MANAGER")
    frame={k:None for k in SLOTS}
    turns=["I need a relief camp","I am in Ward 4"]
    for u in turns:
        answer,frame,state=respond(frame,u); print("Citizen:",u,"\nAgent:",answer,"\nState:",state,"\nFrame:",frame)
    frame={k:None for k in SLOTS}
    for u in ["I need a camp in Ward 5","No, Ward 6"]:
        answer,frame,state=respond(frame,u); print("\nCitizen:",u,"\nAgent:",answer,"\nFrame:",frame)
    print("\nFinite states: START -> ASK_NEED -> ASK_AREA -> CONFIRM/COMPLETE; any state -> CANCELLED; emergency -> ESCALATE.")
if __name__=="__main__": main()

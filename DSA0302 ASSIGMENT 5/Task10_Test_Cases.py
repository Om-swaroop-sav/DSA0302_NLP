"""Task 10: small reproducible sanity checks for the supplied demo components."""
from Task01_Discourse_Segmentation import segment_report
from Task02_Reference_Resolution import hobbs_demo, TREES, muc_score, bcubed
from Task04_Discourse_Structure import parse_two_sentences
from Task05_Dialogue_Manager import respond, SLOTS
from Task09_Machine_Translation import ibm1_em, PARALLEL
from common import REPORTS
def main():
    assert len(segment_report(REPORTS[0]))>=2
    assert hobbs_demo(TREES[0][1])=="tree"
    assert parse_two_sentences("Rain fell. Therefore roads flooded.")["relation"]=="RESULT"
    frame={k:None for k in SLOTS}
    _,frame,state=respond(frame,"I need a camp in Ward 4")
    assert frame["area"]=="ward 4"
    assert muc_score([{"a","b"}],[{"a","b"}])[2]==1.0
    assert bcubed([{"a","b"}],[{"a","b"}])[2]==1.0
    assert len(ibm1_em(PARALLEL,2))>0
    print("All demonstration sanity tests passed.")
if __name__=="__main__": main()

"""Task 6: dialogue-act tagset and optional scikit-learn text classifier."""
from common import DIALOGUES
def rule_features(text):
    t=text.lower().strip()
    if any(w in t for w in ["flood","rising","dangerous","warning"]): return "ALERT"
    if t.endswith("?") and t.startswith(("why","how","where","when","is","are","can","could")): return "QUESTION"
    if any(w in t for w in ["please send","please help"]): return "REQUEST_ACTION"
    if t in {"yes","yes.","okay","correct"}: return "CONFIRM"
    if t in {"no","no."} or t.startswith("no,"): return "CORRECT"
    if "thank" in t: return "THANK"
    if "sorry" in t: return "APOLOGY"
    if "hello" in t or "good morning" in t: return "GREETING"
    if "goodbye" in t: return "GOODBYE"
    if "repeat" in t: return "REPEAT_REQUEST"
    if "do not know" in t: return "CANNOT_ANSWER"
    if "wait there" in t or "keep away" in t: return "INSTRUCT"
    return "INFORM"
def main():
    print("TASK 6 - DIALOGUE ACTS")
    tags=sorted({tag for _,tag in DIALOGUES})
    print("Tagset represented in demo:",tags)
    for text,gold in DIALOGUES:
        print(f"{text:42} gold={gold:16} rule_demo={rule_features(text)}")
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import make_pipeline
        X=[x for x,y in DIALOGUES]; y=[y for x,y in DIALOGUES]
        model=make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression(max_iter=1000))
        model.fit(X,y)
        print("\nTraining-set predictions (not held-out accuracy):")
        print(list(zip(X,model.predict(X))))
    except ImportError:
        print("\nInstall scikit-learn to run the classifier: python -m pip install scikit-learn")
    print("This small labelled set is a runnable demonstration, not the required 100-dialogue evaluation.")
if __name__=="__main__": main()

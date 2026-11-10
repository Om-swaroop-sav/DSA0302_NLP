"""Task 12: Evaluate unseen station names and code-mixed transport queries."""
from common import tokenize, read_lines
from task7 import tag_sentence

NEW_CALLS=[
    "is the train to arakkonam on time",
    "Chennai to Madurai bus timing enna",
    "Tambaram station ku train eppo varum"
]
GAZETTEER={"vellore","chennai","madurai","coimbatore","arakkonam","tambaram","egmore"}

def main():
    train=read_lines("train.txt",["two tickets to vellore","bus timing to chennai"])
    vocabulary={w for sentence in train for w in tokenize(sentence)}
    for sentence in NEW_CALLS:
        words=tokenize(sentence)
        unknown=[w for w in words if w not in vocabulary]
        stations=[w for w in words if w in GAZETTEER]
        print("\\nInput:",sentence)
        print("Tokens:",words)
        print("OOV words:",unknown)
        print("Gazetteer matches:",stations)
        print("Rule POS tags:",tag_sentence(sentence))
        print("LM vocabulary mapping:",[w if w in vocabulary else "<UNK>" for w in words])
    print("\\nSuggested adaptation: update the station gazetteer, add code-mixed training data,")
    print("use character/subword features for unknown words, and evaluate on a separate new-domain test set.")

if __name__=="__main__":
    main()

"""Task 9: Transformation-based Brill POS tagger using NLTK."""
from common import read_tagged

def main():
    try:
        from nltk.tag import DefaultTagger, UnigramTagger, brill
        from nltk.tag.brill_trainer import BrillTaggerTrainer
    except ImportError:
        print("Install NLTK: pip install nltk")
        return
    train=read_tagged("tagged_train.txt")
    test=read_tagged("tagged_test.txt")
    if not train:
        print("Create tagged_train.txt first.")
        return
    templates=[
        brill.Template(brill.Pos([-1])),
        brill.Template(brill.Pos([1])),
        brill.Template(brill.Pos([-2])),
        brill.Template(brill.Pos([2])),
        brill.Template(brill.Pos([-2,-1])),
        brill.Template(brill.Pos([1,2]))
    ]
    baseline=DefaultTagger("NN")
    initial=UnigramTagger(train,backoff=baseline)
    trainer=BrillTaggerTrainer(initial,templates,trace=0)
    tagger=trainer.train(train,max_rules=10,min_score=1)
    print("Learned transformations:")
    for rule in tagger.rules()[:10]: print(rule)
    if test:
        print(f"Held-out accuracy: {tagger.accuracy(test)*100:.2f}%")
    else:
        print("Add tagged_test.txt to calculate held-out accuracy.")

if __name__=="__main__":
    main()

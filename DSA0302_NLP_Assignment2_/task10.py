"""Task 10: Run evaluation, timing and plots for language models and taggers."""
import time
from pathlib import Path
from task5 import evaluate_unigram
from common import read_lines, read_tagged
from task7 import tag_sentence
from task8 import HMMTagger

DEMO_TRAIN=["two tickets to vellore","book a ticket to madurai",
            "what is the bus fare to chennai"]
DEMO_TEST=["two tickets to chennai","when is the next train"]

def main():
    train=read_lines("train.txt",DEMO_TRAIN)
    dev=read_lines("dev.txt",DEMO_TEST)
    test=read_lines("test.txt",DEMO_TEST)
    start=time.perf_counter()
    for _ in range(10): evaluate_unigram(train,dev)
    print(f"10 unigram evaluations: {time.perf_counter()-start:.6f} seconds")
    h,pp=evaluate_unigram(train,test)
    print(f"Test cross-entropy={h:.4f}; perplexity={pp:.4f}")

    tagged_train=read_tagged("tagged_train.txt")
    tagged_test=read_tagged("tagged_test.txt")
    if tagged_train and tagged_test:
        hmm=HMMTagger(tagged_train)
        start=time.perf_counter()
        for sent in tagged_test: hmm.viterbi([w for w,_ in sent])
        print(f"HMM test tagging time: {time.perf_counter()-start:.6f} seconds")

    try:
        import matplotlib.pyplot as plt
        plt.figure()
        plt.bar(["Unigram"],[pp])
        plt.ylabel("Perplexity"); plt.title("Language model test perplexity")
        plt.tight_layout(); plt.savefig("task10_perplexity.png"); plt.close()
        print("Saved task10_perplexity.png")
    except ImportError:
        print("Install matplotlib to generate plots.")
    print("For the full assignment, also record hardware, model size, all model scores and tagger speed.")

if __name__=="__main__":
    main()

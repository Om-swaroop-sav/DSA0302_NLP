"""Task 8: Hidden Markov Model POS tagger with Viterbi decoding."""
import math
from collections import Counter
from common import read_tagged, tokenize

class HMMTagger:
    def __init__(self, tagged_sentences, alpha=0.1):
        self.alpha = alpha
        self.tag_counts, self.emissions, self.transitions = Counter(),Counter(),Counter()
        self.vocab, self.tags = set(),set()
        for sent in tagged_sentences:
            tag_sequence = ["<s>"] + [tag for _,tag in sent] + ["</s>"]
            for word,tag in sent:
                self.tag_counts[tag]+=1
                self.emissions[(tag,word.lower())]+=1
                self.vocab.add(word.lower()); self.tags.add(tag)
            for a,b in zip(tag_sequence,tag_sequence[1:]):
                self.transitions[(a,b)]+=1

    def transition(self, previous, current):
        numerator = self.transitions[(previous,current)] + self.alpha
        denominator = sum(v for (a,_),v in self.transitions.items() if a==previous)
        return numerator/(denominator+self.alpha*(len(self.tags)+1))

    def emission(self, word, tag):
        numerator = self.emissions[(tag,word.lower())]+self.alpha
        denominator = self.tag_counts[tag]+self.alpha*(len(self.vocab)+1)
        return numerator/denominator

    def viterbi(self, words):
        if not words or not self.tags: return []
        tags = sorted(self.tags)
        scores, back = [{}], [{}]
        for tag in tags:
            scores[0][tag] = (math.log(self.transition("<s>",tag))+
                              math.log(self.emission(words[0],tag)))
            back[0][tag] = None
        for i in range(1,len(words)):
            scores.append({}); back.append({})
            for tag in tags:
                candidates = [(scores[i-1][prev]+
                               math.log(self.transition(prev,tag))+
                               math.log(self.emission(words[i],tag)),prev)
                              for prev in tags]
                scores[i][tag],back[i][tag]=max(candidates)
        last=max(tags,key=lambda t:scores[-1][t]+math.log(self.transition(t,"</s>")))
        sequence=[last]
        for i in range(len(words)-1,0,-1):
            sequence.append(back[i][sequence[-1]])
        sequence.reverse()
        return list(zip(words,sequence))

def main():
    train=read_tagged("tagged_train.txt")
    if not train:
        print("Create tagged_train.txt with token<TAB>tag rows and blank lines between sentences.")
        return
    model=HMMTagger(train)
    words=tokenize("two tickets to vellore")
    print("Viterbi tags:",model.viterbi(words))
    gold=read_tagged("tagged_test.txt")
    if gold:
        correct=total=0
        for sent in gold:
            predicted=model.viterbi([w for w,_ in sent])
            for p,g in zip(predicted,sent):
                correct += p[1]==g[1]; total+=1
        print(f"Held-out accuracy: {100*correct/total:.2f}%" if total else "No test tokens.")

if __name__=="__main__":
    main()

def main():
    try:
        from nltk import pos_tag, word_tokenize, RegexpParser
        from nltk.corpus import wordnet as wn
        sentence = "The intelligent doctor reviews patient records in the hospital."
        tagged = pos_tag(word_tokenize(sentence))
        tree = RegexpParser("NP: {<DT>?<JJ.*>*<NN.*>+}").parse(tagged)
        phrases = []
        for subtree in tree.subtrees(lambda node: node.label() == "NP"):
            phrase = " ".join(word for word, _ in subtree.leaves())
            phrases.append(phrase)
        print("Sentence:", sentence)
        print("Noun phrases and head-word meanings:")
        for phrase in phrases:
            head = phrase.split()[-1].lower()
            synsets = wn.synsets(head, pos=wn.NOUN)
            meaning = synsets[0].definition() if synsets else "No WordNet definition found"
            print(f"{phrase} -> head={head}: {meaning}")
    except ImportError:
        print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")
    except LookupError:
        print("SKIPPED: NLTK tagger/tokenizer/WordNet data missing. Run setup_nltk.ps1.")

if __name__ == "__main__":
    main()

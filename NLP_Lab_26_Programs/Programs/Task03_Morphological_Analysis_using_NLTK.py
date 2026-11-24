def main():
    try:
        import nltk
        from nltk.stem import WordNetLemmatizer
        from nltk import pos_tag, word_tokenize
        tokens = word_tokenize("The students were studying medical records carefully.")
        tagged = pos_tag(tokens)
        lemmatizer = WordNetLemmatizer()
        print("Word | POS | lemma/root | feature")
        for word, tag in tagged:
            wn_pos = "v" if tag.startswith("V") else "a" if tag.startswith("J") else "r" if tag.startswith("R") else "n"
            root = lemmatizer.lemmatize(word.lower(), wn_pos)
            feature = "plural noun" if tag == "NNS" else "past verb" if tag == "VBD" else "third-person verb" if tag == "VBZ" else "-"
            print(f"{word} | {tag} | {root} | {feature}")
    except LookupError as exc:
        print("SKIPPED: NLTK data is missing. Run setup_nltk.ps1. Details:", str(exc).splitlines()[0])
    except ImportError:
        print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

if __name__ == "__main__":
    main()

def main():
    try:
        from nltk import pos_tag, word_tokenize
        sentence = "The intelligent student writes Python programs for language analysis."
        tokens = word_tokenize(sentence)
        print("Sentence:", sentence)
        print("POS tags:")
        for word, tag in pos_tag(tokens):
            print(f"{word:15} {tag}")
    except LookupError as exc:
        print("SKIPPED: NLTK tokenizer/tagger data missing. Run setup_nltk.ps1. Details:", str(exc).splitlines()[0])
    except ImportError:
        print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

if __name__ == "__main__":
    main()

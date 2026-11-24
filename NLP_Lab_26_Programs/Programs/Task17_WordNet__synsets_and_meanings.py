def main():
    try:
        from nltk.corpus import wordnet as wn
        word = "bank"
        synsets = wn.synsets(word)
        print("Word:", word)
        for syn in synsets[:6]:
            print(f"{syn.name()} | {syn.pos()} | {syn.definition()}")
    except ImportError:
        print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")
    except LookupError:
        print("SKIPPED: WordNet corpus is missing. Run setup_nltk.ps1.")

if __name__ == "__main__":
    main()

def main():
    try:
        from nltk.wsd import lesk
        from nltk.tokenize import word_tokenize
        sentence = "She deposited money at the bank beside the river."
        context = word_tokenize(sentence)
        sense = lesk(context, "bank", "n")
        print("Sentence:", sentence)
        print("Target word: bank")
        print("Selected sense:", sense.name() if sense else "No sense selected")
        print("Definition:", sense.definition() if sense else "Unavailable")
    except ImportError:
        print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")
    except LookupError:
        print("SKIPPED: NLTK tokenizer/WordNet data missing. Run setup_nltk.ps1.")

if __name__ == "__main__":
    main()

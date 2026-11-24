def main():
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        text = "Satya Nadella visited Microsoft in London on Monday."
        doc = nlp(text)
        print("Text:", text)
        for ent in doc.ents:
            print(f"{ent.text:20} {ent.label_:15} {spacy.explain(ent.label_)}")
    except ImportError:
        print("SKIPPED: spaCy is not installed. Run setup_core.ps1.")
    except OSError:
        print("SKIPPED: spaCy model en_core_web_sm is missing. Run: python -m spacy download en_core_web_sm")

if __name__ == "__main__":
    main()

def main():
    try:
        from transformers import pipeline
        # First execution may download this English-to-French model from Hugging Face.
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        text = "Natural language processing helps computers understand human language."
        result = translator(text, max_length=128)
        print("English:", text)
        print("French:", result[0]["translation_text"])
    except ImportError:
        print("SKIPPED: Transformers is not installed. Run setup_translation.ps1 (large download).")
    except Exception as exc:
        print("SKIPPED: Translation model could not be loaded or downloaded:", type(exc).__name__, str(exc))
        print("Check the internet connection and retry after running setup_translation.ps1.")

if __name__ == "__main__":
    main()

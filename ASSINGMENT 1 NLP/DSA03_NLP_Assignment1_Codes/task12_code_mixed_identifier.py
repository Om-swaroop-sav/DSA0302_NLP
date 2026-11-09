ENGLISH_WORDS = {
    "patient", "fever", "paracetamol", "medicine", "hospital", "doctor"
}

ROMANISED_TAMIL_WORDS = {
    "ku", "irundhuchu", "kuduthen", "vandhu", "sapten"
}

def identify_tokens(text):
    for word in text.lower().split():
        clean = word.strip(".,!?;:")
        if clean in ENGLISH_WORDS:
            language = "English"
        elif clean in ROMANISED_TAMIL_WORDS:
            language = "Romanised Tamil"
        else:
            language = "Unknown"
        print(f"{clean} -> {language}")

if __name__ == "__main__":
    sample = "patient ku fever irundhuchu paracetamol kuduthen"
    identify_tokens(sample)

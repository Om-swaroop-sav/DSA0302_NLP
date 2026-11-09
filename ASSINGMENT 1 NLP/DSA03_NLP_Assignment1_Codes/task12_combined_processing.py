import re

CORRECTIONS = {
    "5OOmg": "500mg",
    "paracetarnol": "paracetamol",
}

ENGLISH_WORDS = {
    "patient", "fever", "paracetamol", "medicine", "hospital"
}

ROMANISED_TAMIL_WORDS = {
    "ku", "irundhuchu", "kuduthen"
}

def process_text(text):
    for wrong, correct in CORRECTIONS.items():
        text = text.replace(wrong, correct)

    # Preserve medicine strengths as one token.
    tokens = re.findall(
        r"\d+(?:\.\d+)?(?:mg|mcg|ml|g)|[A-Za-z]+",
        text,
        flags=re.IGNORECASE,
    )

    print("Corrected text:", text)
    print("\nToken analysis:")
    for token in tokens:
        word = token.lower()
        if word in ENGLISH_WORDS:
            label = "English"
        elif word in ROMANISED_TAMIL_WORDS:
            label = "Romanised Tamil"
        elif re.fullmatch(r"\d+(?:\.\d+)?(?:mg|mcg|ml|g)", word):
            label = "Dosage"
        else:
            label = "Unknown"
        print(f"{token} -> {label}")

if __name__ == "__main__":
    sample = "patient ku fever irundhuchu 5OOmg paracetarnol kuduthen"
    process_text(sample)

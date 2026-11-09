def correct_ocr(text):
    # Only use context-verified replacements. Blind replacement can corrupt valid text.
    corrections = {
        "5OOmg": "500mg",
        "paracetarnol": "paracetamol",
        "Medica1": "Medical",
        "Mornlng": "Morning",
        "Norrnal": "Normal",
    }
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    return text

if __name__ == "__main__":
    sample = "Patient received 5OOmg paracetarnol."
    print("Original:", sample)
    print("Corrected:", correct_ocr(sample))

import re

TOKEN_PATTERN = re.compile(
    r"\d+(?:\.\d+)?(?:mg/dL|mmol/L|mg|mcg|ml|g|°C|°F)"
    r"|[A-Za-z]+(?:[-'][A-Za-z]+)*(?:\.[A-Za-z]+)*"
    r"|\d+(?:\.\d+)?"
    r"|[^\w\s]",
    flags=re.IGNORECASE,
)

def tokenize(text):
    """Longest-first token pattern for common clinical tokens."""
    return TOKEN_PATTERN.findall(text)

ABBREVIATIONS = {
    "BP": "blood pressure",
    "HR": "heart rate",
    "HTN": "hypertension",
    "DM": "diabetes mellitus",
    "OD": "once daily",
    "BID": "twice daily",
    "TID": "three times daily",
    "PRN": "as needed",
}

def normalize(text):
    text = text.lower()
    for short, full in ABBREVIATIONS.items():
        text = re.sub(
            rf"(?<!\w){re.escape(short.lower())}(?!\w)",
            full,
            text,
            flags=re.IGNORECASE,
        )
    text = re.sub(r"(?i)(\d+(?:\.\d+)?)mg\b", r"\1 mg", text)
    text = re.sub(r"(?i)(\d+(?:\.\d+)?)ml\b", r"\1 mL", text)
    return text

if __name__ == "__main__":
    sample = "Patient received 500mg paracetamol twice-daily. BP normal; medicine BID."
    print("Original:", sample)
    print("Tokens:", tokenize(sample))
    print("Normalised:", normalize(sample))

import re
import time
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

TOKEN_PATTERN = re.compile(
    r"\d+(?:\.\d+)?(?:mg/dL|mmol/L|mg|mcg|ml|g|°C|°F)"
    r"|[A-Za-z]+(?:[-'][A-Za-z]+)*(?:\.[A-Za-z]+)*"
    r"|\d+(?:\.\d+)?"
    r"|[^\w\s]",
    re.IGNORECASE,
)

PATTERNS = {
    "Patient ID": r"\bPAT-\d{6}\b",
    "Date": r"\b(?:0[1-9]|[12]\d|3[01])[-/](?:0[1-9]|1[0-2])[-/](?:19|20)\d{2}\b",
    "Drug": r"\b[A-Za-z][A-Za-z-]*\s+\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml)\b",
    "Blood Pressure": r"\b\d{2,3}/\d{2,3}\s*mmHg\b",
    "Temperature": r"\b\d{2}(?:\.\d+)?\s*°?C\b",
    "Contact": r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",
    "Age": r"\b(?:[1-9]\d?|1[01]\d|120)\s*(?:years?|yrs?)\b",
    "Frequency": r"\b(?:once|twice|thrice)\s+daily\b",
}

MORPHOLOGY = {
    "fractures": "fracture +N +PL",
    "patients": "patient +N +PL",
    "treated": "treat +V +PAST",
    "treating": "treat +V +PROGRESSIVE",
    "infections": "infection +N +PL",
}

def process_record(text):
    start = time.perf_counter()
    tokens = TOKEN_PATTERN.findall(text)

    entities = {
        label: re.findall(pattern, text, flags=re.IGNORECASE)
        for label, pattern in PATTERNS.items()
    }

    analyses = {
        token: MORPHOLOGY.get(token.lower(), "Unknown")
        for token in tokens if token.isalpha()
    }

    stems = {
        token: stemmer.stem(token)
        for token in tokens if token.isalpha()
    }

    elapsed = time.perf_counter() - start
    return {
        "tokens": tokens,
        "entities": entities,
        "analyses": analyses,
        "stems": stems,
        "runtime_seconds": elapsed,
    }

if __name__ == "__main__":
    record = """
    PAT-123456 Patient aged 45 years admitted on 12/05/2026.
    Patient has fractures and infections.
    Paracetamol 500mg given twice daily.
    Blood pressure 120/80 mmHg. Temperature 37.5°C.
    """

    result = process_record(record)
    for section, value in result.items():
        print(f"\n{section.upper()}:")
        print(value)

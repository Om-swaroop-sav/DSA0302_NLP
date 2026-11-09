import re

text = """
Patient ID: PAT-123456
Admission: 12/05/2026
Discharge: 15/05/2026
Drug: Paracetamol 500mg
Frequency: twice daily
Glucose: 120 mg/dL
BP: 120/80 mmHg
Temperature: 37.5°C
ICD: S72.001A
Ward A1, Bed 12
Contact: 9876543210
Age: 45 years
"""

patterns = {
    "Patient ID": r"\bPAT-\d{6}\b",
    "Date": r"\b(?:0[1-9]|[12]\d|3[01])[-/](?:0[1-9]|1[0-2])[-/](?:19|20)\d{2}\b",
    "Drug Strength": r"\b[A-Za-z][A-Za-z-]*\s+\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml)\b",
    "Frequency": r"\b(?:once|twice|thrice)\s+daily\b",
    "Lab Value": r"\b[A-Za-z]+:\s*\d+(?:\.\d+)?\s*(?:mg/dL|mmol/L|g/dL)\b",
    "Blood Pressure": r"\b\d{2,3}/\d{2,3}\s*mmHg\b",
    "Temperature": r"\b\d{2}(?:\.\d+)?\s*°?[CF]\b",
    "ICD Code": r"\b[A-TV-Z]\d[A-Z0-9](?:\.[A-Z0-9]{1,4})?\b",
    "Ward and Bed": r"\bWard\s+[A-Z0-9-]+,\s*Bed\s+[A-Z0-9-]+\b",
    "Contact": r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",
    "Age": r"\b(?:[1-9]\d?|1[01]\d|120)\s*(?:years?|yrs?)\b",
}

for name, pattern in patterns.items():
    print(f"{name}: {re.findall(pattern, text, flags=re.IGNORECASE)}")

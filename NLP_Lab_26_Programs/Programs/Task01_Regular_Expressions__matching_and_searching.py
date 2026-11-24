import re

text = "Patient record: ID 2026, email om@example.com, phone 9876543210."
patterns = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "10-digit phone": r"\b\d{10}\b",
    "record ID": r"\bID\s+\d{4}\b",
}
print("Text:", text)
for label, pattern in patterns.items():
    match = re.search(pattern, text)
    print(f"{label}: {match.group(0) if match else 'not found'}")
print("All digit sequences:", re.findall(r"\d+", text))

import re
text = """Call +91 98765 43210 or 555-123-4567. Meeting is on 15-08-2024 and 2023-12-25."""
dates = re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b|\b\d{4}[-/]\d{2}[-/]\d{2}\b', text)
phones = re.findall(r'\+?\d{2,3}[- ]?\d{5}[- ]?\d{5}|\d{3}[-]\d{3}[-]\d{4}', text)
print("Dates:", dates)
print("Phone Numbers:", phones)

"""Task 4: transparent rule-based NER baseline."""
import re
PATTERNS={'DATE':r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|(?:19|20)\d{2})\b','MONEY':r'\b(?:Rs\.?|INR)\s?\d+(?:,\d{3})*(?:\.\d{1,2})?\b','PENSION_SCHEME':r'\b(?:family pension|retirement pension|revised pension scheme|pension scheme)\b','DOCUMENT':r'\b(?:circular|memorandum|government order|G\.O\.)\s*(?:No\.?\s*)?[A-Z0-9/-]*','PERSON':r'\b(?:Mr\.|Ms\.|Mrs\.|Shri)\s+[A-Z][a-z]+\b','ORGANISATION':r'\b(?:Pension Directorate|Treasury Department|Finance Department)\b'}
def extract_entities(text):
    out=[]
    for typ,pat in PATTERNS.items():
        for m in re.finditer(pat,text,re.I): out.append({'text':m.group(),'type':typ,'start':m.start(),'end':m.end()})
    return sorted(out,key=lambda x:x['start'])
def entity_counts(docs):
    c={}
    for d in docs:
        for e in extract_entities(d.get('text','')): c[e['type']]=c.get(e['type'],0)+1
    return c

if __name__ == "__main__":
    examples = [
        "Mr. Ravi retired in 2019 under the family pension circular No. 12/2020.",
        "The Finance Department issued a revised pension scheme effective 01/04/2021.",
        "Shri Kumar receives INR 25,000 under retirement pension."
    ]
    for sentence in examples:
        print("\nTEXT:", sentence)
        for entity in extract_entities(sentence):
            print(f"{entity['text']} -> {entity['type']} (start={entity['start']}, end={entity['end']})")
    print("\nTask 4 NER demo completed.")

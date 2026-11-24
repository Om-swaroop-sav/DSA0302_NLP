import re

text = "Ravi gave Meena a book because she needed it. He also sent a note to her."
# Small demonstrator: resolve gender/number pronouns to the most recent compatible noun.
known = [
    ("Ravi", "male"), ("Meena", "female"), ("book", "neutral"), ("note", "neutral")
]
pronouns = {"he": "male", "him": "male", "she": "female", "her": "female", "it": "neutral"}
words = re.findall(r"[A-Za-z]+", text)
seen = []
for word in words:
    lower = word.lower()
    if lower in pronouns:
        expected = pronouns[lower]
        candidates = [name for name, gender in seen if gender == expected]
        antecedent = candidates[-1] if candidates else "unresolved"
        print(f"{word} -> {antecedent}")
    else:
        match = next(((name, gender) for name, gender in known if name.lower() == lower), None)
        if match:
            seen.append(match)

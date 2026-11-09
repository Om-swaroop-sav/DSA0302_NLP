def add_suffix(word, suffix):
    """Simplified teaching rules; not a complete English morphology engine."""

    # Consonant + y -> i before selected suffixes.
    if suffix in {"es", "ed", "er", "est"} and word.endswith("y"):
        if len(word) > 1 and word[-2].lower() not in "aeiou":
            word = word[:-1] + "i"

    # Final e is dropped before -ing, except selected forms such as be.
    if suffix == "ing" and word.endswith("e") and word not in {"be", "see"}:
        word = word[:-1]

    # Sibilant plural: add -es.
    if suffix == "s" and word.endswith(("s", "sh", "ch", "x", "z")):
        suffix = "es"

    # Simplified CVC doubling for short words before -ing.
    if suffix == "ing" and len(word) == 3:
        a, b, c = word.lower()
        if a.isalpha() and b in "aeiou" and c.isalpha():
            if c not in "aeiouwxy":
                word += word[-1]

    return word + suffix

if __name__ == "__main__":
    tests = [
        ("operate", "ing"),
        ("study", "es"),
        ("stop", "ing"),
        ("happy", "er"),
        ("watch", "s"),
        ("treat", "ed"),
        ("treat", "ing"),
    ]
    for stem, suffix in tests:
        print(f"{stem} + {suffix} -> {add_suffix(stem, suffix)}")

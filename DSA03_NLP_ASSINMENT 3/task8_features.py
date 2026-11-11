"""Task 8: Feature structures and unification.
Run: python task8_features.py
Uses dictionaries to represent feature structures.
"""

def unify(feature_a, feature_b):
    """Return merged compatible features; return None on conflict."""
    result = dict(feature_a)
    for key, value in feature_b.items():
        if key in result and result[key] != value:
            return None
        result[key] = value
    return result

def check_subject_verb(subject, verb):
    merged = unify(subject, verb)
    return merged is not None

def check_determiner_noun(determiner, noun):
    merged = unify(determiner, noun)
    return merged is not None

def main():
    print("FEATURE STRUCTURE UNIFICATION")
    examples = [
        ({"NUM": "singular"}, {"NUM": "singular", "PERSON": 3}),
        ({"CASE": "nominative", "PERSON": 3},
         {"CASE": "nominative", "NUM": "singular"}),
        ({"NUM": "singular"}, {"NUM": "plural"}),
    ]
    for i, (a, b) in enumerate(examples, 1):
        print(f"\nExample {i}")
        print("Feature A:", a)
        print("Feature B:", b)
        print("Unification:", unify(a, b))

    print("\nSUBJECT-VERB AGREEMENT")
    subjects = {
        "student": {"NUM": "singular", "PERSON": 3},
        "students": {"NUM": "plural", "PERSON": 3},
    }
    verbs = {
        "submits": {"NUM": "singular", "PERSON": 3},
        "submit": {"NUM": "plural", "PERSON": 3},
    }
    for subject, sf in subjects.items():
        for verb, vf in verbs.items():
            print(f"{subject} + {verb}:",
                  "VALID" if check_subject_verb(sf, vf) else "INVALID")

    print("\nDETERMINER-NOUN AGREEMENT")
    print("this + room:", check_determiner_noun(
        {"NUM": "singular"}, {"NUM": "singular"}))
    print("these + rooms:", check_determiner_noun(
        {"NUM": "plural"}, {"NUM": "plural"}))
    print("these + room:", check_determiner_noun(
        {"NUM": "plural"}, {"NUM": "singular"}))

if __name__ == "__main__":
    main()

# Small teaching lexicon: surface form -> all possible lexical analyses.

LEXICON = {
    "fractures": ["fracture +N +PL"],
    "patients": ["patient +N +PL"],
    "treated": ["treat +V +PAST", "treat +V +PAST_PARTICIPLE"],
    "treating": ["treat +V +PROGRESSIVE"],
    "infections": ["infection +N +PL"],
    "studies": ["study +N +PL", "study +V +3SG"],
}

# One lexical-to-surface relation, used in either direction.
FST = {
    "fracture +N +PL": "fractures",
    "patient +N +PL": "patients",
    "treat +V +PAST": "treated",
    "treat +V +PROGRESSIVE": "treating",
    "infection +N +PL": "infections",
}

def parse(surface):
    return LEXICON.get(surface.lower(), ["Unknown"])

def generate(lexical):
    return FST.get(lexical, "Not found")

if __name__ == "__main__":
    for word in ["fractures", "patients", "treated", "treating",
                 "infections", "studies", "unknown"]:
        print(f"{word} -> {parse(word)}")

    print("\nGeneration:")
    print("fracture +N +PL ->", generate("fracture +N +PL"))

IRREGULAR = {"child": "children", "man": "men", "woman": "women", "person": "people", "mouse": "mice"}

def plural(noun: str) -> str:
    lower = noun.lower()
    if lower in IRREGULAR:
        result = IRREGULAR[lower]
    elif lower.endswith(("s", "x", "z", "ch", "sh")):
        result = lower + "es"
    elif len(lower) > 1 and lower.endswith("y") and lower[-2] not in "aeiou":
        result = lower[:-1] + "ies"
    else:
        result = lower + "s"
    return result

for noun in ["book", "bus", "box", "church", "baby", "city", "child", "mouse"]:
    print(f"{noun} -> {plural(noun)}")

# 4. Finite-State Morphological Parser
words = ["writes", "writing", "written"]
data = {
    "writes": ("write", "write + s", "Regular inflection", ["START", "ROOT_CHECK", "SUFFIX_S", "ACCEPT"]),
    "writing": ("write", "write + ing (drop final e)", "Regular inflection", ["START", "ROOT_CHECK", "SUFFIX_ING", "DROP_E", "ACCEPT"]),
    "written": ("write", "irregular participle form", "Irregular inflection", ["START", "ROOT_CHECK", "IRREGULAR_FORM", "ACCEPT"]),
}
print(f"{'Word':<10}{'State path':<55}{'Breakdown':<34}{'Root':<10}{'Class'}")
print("-" * 125)
for word in words:
    root, breakdown, kind, path = data[word]
    print(f"{word:<10}{' -> '.join(path):<55}{breakdown:<34}{root:<10}{kind}")



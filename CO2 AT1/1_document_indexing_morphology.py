
words = ["connected", "connecting", "connection"]
data = {
    "connected": ("connect", "ed", "Inflectional (past tense)"),
    "connecting": ("connect", "ing", "Inflectional (present participle)"),
    "connection": ("connect", "ion", "Derivational (noun-forming)"),
}
print(f"{'Word':<14}{'Root':<12}{'Suffix':<10}{'Type':<36}{'Normalized'}")
print("-" * 85)
for word in words:
    root, suffix, kind = data[word]
    print(f"{word:<14}{root:<12}{suffix:<10}{kind:<36}{root}")


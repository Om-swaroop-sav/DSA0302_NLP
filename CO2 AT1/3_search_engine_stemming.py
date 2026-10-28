# 3. Stemming-Based Preprocessing for a Search Engine
words = ["played", "player", "playing"]
data = {
    "played": ("play", "ed", "Inflectional", "play"),
    "player": ("play", "er", "Derivational (person noun)", "play"),
    "playing": ("play", "ing", "Inflectional (participle/gerund)", "play"),
}
print(f"{'Word':<12}{'Stem':<10}{'Removed affix':<15}{'Transformation':<38}{'Normalized'}")
print("-" * 95)
for word in words:
    stem, affix, kind, normalized = data[word]
    print(f"{word:<12}{stem:<10}{affix:<15}{kind:<38}{normalized}")


def plural(word):
    if word.endswith("s"):
        return word + "es"
    elif word.endswith("sh") or word.endswith("ch"):
        return word + "es"
    elif word.endswith("x"):
        return word + "es"
    elif word.endswith("y"):
        return word[:-1] + "ies"
    else:
        return word + "s"
words = ["cat", "dog", "box", "bus", "brush", "baby"]
for word in words:
    print("Singular:", word)
    print("Plural:", plural(word))
    print()

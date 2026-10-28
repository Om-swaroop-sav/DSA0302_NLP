import re
strings = ["cat", "cats", "cattt", "dog", "apple", "123cat"]
patterns = [r"cat?", r"cat*", r"cat+", r"[a-z]+", r"[^0-9]+", r"^cat", r"cat$"]
for pattern in patterns:
    print("\nPattern:", pattern)
    for text in strings:
        if re.search(pattern, text):
            print(text, "YES")
        else:
            print(text, "NO")

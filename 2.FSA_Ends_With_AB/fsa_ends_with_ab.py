def fsa(s):
    state = "q0"
    path = [state]
    for ch in s:
        if state == "q0":
            state = "q1" if ch == "a" else "q0"
        elif state == "q1":
            state = "q2" if ch == "b" else "q1"
        else:
            state = "q1" if ch == "a" else "q0"
        path.append(state)
    print(s, "->", " -> ".join(path), "YES" if state == "q2" else "NO")
for s in ["ab", "aab", "aba", "abb", "bba"]:
    fsa(s)

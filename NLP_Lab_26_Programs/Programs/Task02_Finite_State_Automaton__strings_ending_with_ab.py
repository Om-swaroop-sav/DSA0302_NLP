def accepts_ending_ab(value: str) -> bool:
    # q0: no useful suffix; q1: latest character is a; q2: suffix is ab.
    state = "q0"
    transitions = {
        ("q0", "a"): "q1", ("q0", "b"): "q0",
        ("q1", "a"): "q1", ("q1", "b"): "q2",
        ("q2", "a"): "q1", ("q2", "b"): "q0",
    }
    for symbol in value:
        if symbol not in "ab":
            return False
        state = transitions[(state, symbol)]
    return state == "q2"

samples = ["ab", "aab", "babab", "aba", "abb", "", "acb"]
for sample in samples:
    print(f"{sample!r}: {'ACCEPT' if accepts_ending_ab(sample) else 'REJECT'}")

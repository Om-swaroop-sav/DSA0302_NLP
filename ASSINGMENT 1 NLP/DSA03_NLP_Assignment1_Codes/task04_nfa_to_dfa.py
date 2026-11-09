from collections import deque

# NFA for binary strings ending in "01".
# NFA states: A (start), B, C (final).
nfa = {
    "A": {"0": {"A", "B"}, "1": {"A"}},
    "B": {"0": set(), "1": {"C"}},
    "C": {"0": set(), "1": set()},
}
alphabet = {"0", "1"}
start_state = frozenset({"A"})
final_nfa_states = {"C"}

def subset_construction(nfa, alphabet, start, final_states):
    dfa_transitions = {}
    discovered = {start}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        dfa_transitions[current] = {}

        for symbol in sorted(alphabet):
            next_set = set()
            for state in current:
                next_set.update(nfa.get(state, {}).get(symbol, set()))

            next_state = frozenset(next_set)
            dfa_transitions[current][symbol] = next_state

            if next_state not in discovered:
                discovered.add(next_state)
                queue.append(next_state)

    dfa_finals = {
        state for state in discovered
        if state.intersection(final_states)
    }
    return dfa_transitions, start, dfa_finals

def accepts(dfa, start, finals, text):
    state = start
    for symbol in text:
        if symbol not in {"0", "1"}:
            return False
        state = dfa[state][symbol]
    return state in finals

if __name__ == "__main__":
    dfa, dfa_start, dfa_finals = subset_construction(
        nfa, alphabet, start_state, final_nfa_states
    )

    print("DFA transition table:")
    for state, transitions in dfa.items():
        print(f"{set(state)}: ", {
            symbol: set(target)
            for symbol, target in transitions.items()
        })

    print("Final DFA states:", [set(s) for s in dfa_finals])

    for sample in ["01", "101", "0001", "10", "111"]:
        print(sample, "ACCEPT" if accepts(
            dfa, dfa_start, dfa_finals, sample
        ) else "REJECT")

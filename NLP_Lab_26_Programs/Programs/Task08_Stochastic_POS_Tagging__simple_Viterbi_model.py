import math

states = ["DET", "NOUN", "VERB"]
start = {"DET": 0.6, "NOUN": 0.2, "VERB": 0.2}
transition = {
    "DET": {"DET": 0.05, "NOUN": 0.80, "VERB": 0.15},
    "NOUN": {"DET": 0.10, "NOUN": 0.20, "VERB": 0.70},
    "VERB": {"DET": 0.20, "NOUN": 0.30, "VERB": 0.50},
}
emission = {
    "the": {"DET": 0.98, "NOUN": 0.01, "VERB": 0.01},
    "dog": {"DET": 0.01, "NOUN": 0.98, "VERB": 0.01},
    "barks": {"DET": 0.01, "NOUN": 0.09, "VERB": 0.90},
    "a": {"DET": 0.98, "NOUN": 0.01, "VERB": 0.01},
    "cat": {"DET": 0.01, "NOUN": 0.98, "VERB": 0.01},
    "sleeps": {"DET": 0.01, "NOUN": 0.09, "VERB": 0.90},
}
sentence = "the dog barks".split()
score = {}
back = {}
for state in states:
    score[state] = math.log(start[state]) + math.log(emission.get(sentence[0], {}).get(state, 0.01))
    back[state] = []
for word in sentence[1:]:
    new_score, new_back = {}, {}
    for state in states:
        options = [(score[prev] + math.log(transition[prev][state]), prev) for prev in states]
        best, prev = max(options)
        new_score[state] = best + math.log(emission.get(word, {}).get(state, 0.01))
        new_back[state] = back[state] + [prev]
    score, back = new_score, new_back
last = max(score, key=score.get)
tags = back[last] + [last]
print("Tokens:", sentence)
print("Most likely tags:", list(zip(sentence, tags)))

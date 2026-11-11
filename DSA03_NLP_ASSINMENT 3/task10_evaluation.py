"""Task 10: Compare top-down and Earley parsing on 30 queries.
Run: python task10_evaluation.py
Requires task6_top_down.py and task7_earley.py in the same folder.
Optional plot: pip install matplotlib
"""
import time
from task6_top_down import Parser, tokenize as top_tokenize
from task7_earley import earley_parse, tokenize as earley_tokenize

QUERIES = [
    "The student checks the timetable", "The student submits the form",
    "I book a room", "You submit the form", "The exam starts",
    "Om checks the timetable", "The student checks the form",
    "The student book a room", "The student submits a form",
    "I check the timetable", "You book a room", "The student starts",
    "The exam starts near the library", "The student checks the notice",
    "The student checks the form near the library", "Can you book a room",
    "Can I submit the form", "When does the exam start", "Submit the form",
    "Check the timetable", "The student checks the room",
    "The student submits the notice", "I submit the form",
    "You check the exam", "Om submits the form",
    "The student checks the timetable near the library",
    "The student submits the form near the library",
    "The exam starts near the room", "Can you check the timetable",
    "Can I book a room"
]

def main():
    rows = []
    print("ID | SENTENCE | TOP-DOWN | EARLEY | EARLEY STATES | TIME (ms)")
    print("-" * 100)
    for index, sentence in enumerate(QUERIES, 1):
        t0 = time.perf_counter()
        try:
            Parser(top_tokenize(sentence)).parse()
            top_ok = True
        except (ValueError, IndexError):
            top_ok = False
        top_ms = (time.perf_counter() - t0) * 1000

        words = earley_tokenize(sentence)
        t0 = time.perf_counter()
        earley_ok, chart = earley_parse(words)
        earley_ms = (time.perf_counter() - t0) * 1000
        states = sum(len(column) for column in chart)
        rows.append((index, sentence, top_ok, earley_ok, states, top_ms, earley_ms))
        print(f"{index:02d} | {sentence} | {top_ok} | {earley_ok} | "
              f"{states} | {top_ms + earley_ms:.3f}")

    print("\nSUMMARY")
    print("Total queries:", len(rows))
    print("Top-down accepted:", sum(row[2] for row in rows))
    print("Earley accepted:", sum(row[3] for row in rows))
    print("Note: results are for the supplied demonstration grammar, not a full")
    print("40-rule/60-word assignment grammar. Expand grammar and lexicon before")
    print("using these figures as final assignment results.")

    try:
        from importlib import import_module
        plt = import_module("matplotlib.pyplot")
        lengths = [len(sentence.split()) for _, sentence, *_ in rows]
        state_counts = [states for *_, states, top_ms, earley_ms in rows]
        plt.figure(figsize=(8, 5))
        plt.scatter(lengths, state_counts)
        plt.xlabel("Sentence length (words)")
        plt.ylabel("Earley chart states")
        plt.title("Sentence Length vs Earley Chart States")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("task10_chart_states.png", dpi=150)
        print("\nPlot saved as task10_chart_states.png")
    except ImportError:
        print("\nTo generate the plot, install matplotlib: pip install matplotlib")

if __name__ == "__main__":
    main()

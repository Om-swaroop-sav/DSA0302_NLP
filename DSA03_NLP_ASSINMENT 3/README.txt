DSA03 NLP Assignment 3 – Coding Tasks 6 to 10

FILES
task6_top_down.py  - recursive-descent/top-down parser
task7_earley.py    - Earley chart parser (Predictor, Scanner, Completer)
task8_features.py  - feature structures and unification
task9_pcfg.py      - PCFG probabilities and Viterbi CKY demonstration
task10_evaluation.py - compares Task 6 and Task 7 over 30 sample queries

HOW TO RUN
1. Install Python 3.
2. Open this folder in VS Code.
3. Open the terminal in this folder.
4. Run each file separately:
   python task6_top_down.py
   python task7_earley.py
   python task8_features.py
   python task9_pcfg.py
   python task10_evaluation.py

OPTIONAL PLOT
Install matplotlib:
   python -m pip install matplotlib

IMPORTANT ASSIGNMENT NOTE
These are teaching/demo implementations with a compact grammar and lexicon.
The assignment brief requires a larger grammar (at least 40 phrase-structure
rules), a lexicon of at least 60 domain words, and a documented test set.
Expand the grammar and lexicon, annotate the required sample sentences, and
rerun the experiments before reporting final coverage or performance.
Task 9 uses a small CNF-style PCFG and only supports the words/rules listed
inside its RULES table. It is a Viterbi best-tree demonstration.

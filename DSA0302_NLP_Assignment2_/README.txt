DSA03 NLP Assignment 2 - Separate Python files

FILES
- common.py: shared tokenisation, file-reading, splitting and WER helpers
- task1.py: counting, vocabulary thresholds, OOV, Zipf plot
- task2.py: unigram, bigram and trigram models
- task3.py: add-one/add-k and Good-Turing demonstration
- task4.py: backoff and interpolation demonstrations
- task5.py: entropy/perplexity and WER
- task6.py: tagset and Cohen's kappa
- task7.py: rule-based POS tagger (17 rules)
- task8.py: HMM and Viterbi tagger
- task9.py: Brill tagger using NLTK
- task10.py: combined evaluation, timing and plot
- task12.py: new station names, OOV and code-mixed examples

SETUP
1. Extract all files into the same folder.
2. Open that folder in VS Code.
3. Install:
   pip install nltk matplotlib
4. Run an individual task:
   python task1.py
   python task2.py
   ...
   python task12.py

INPUT FILES
Corpus:
- train.txt
- dev.txt
- test.txt
Each line is one utterance.

POS annotation:
- tagged_train.txt
- tagged_test.txt
- double_annotator_a.txt
- double_annotator_b.txt

Each annotation line is:
token<TAB>tag
Use a blank line between sentences. Example:
two    CD
tickets NNS
to     TO
vellore NNP

ACADEMIC NOTES
- Task 11 is comparison and recommendation based on measured outputs; it does not need a separate standalone program.
- Small demonstration data are used if corpus files are absent. These are only for testing code execution, not assignment results.
- The Task 1 lemma function is a suffix heuristic and needs linguistic validation.
- Good-Turing, Katz-style backoff and deleted interpolation are simplified teaching implementations; they are not complete statistical estimators. Do not describe them as full implementations.
- For the assignment, estimate interpolation weights on development data and reserve test data for final evaluation.
- You must supply the required corpus, 200 ASR sets, and manually annotated tokens. The code does not fabricate these.
- Report only actually measured counts, accuracy, perplexity, WER, kappa and runtime.

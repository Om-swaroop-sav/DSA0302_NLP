# DSA03 NLP Assignment 5 (CO5) — Task-wise Python Demonstration

## Files
- Task01: discourse segmentation and cross-sentence reference heuristic
- Task02: simplified Hobbs-style candidate search, Centering Theory, MUC and B-cubed
- Task03: entity grids and transition counts
- Task04: simplified RST-style discourse trees and nucleus summary
- Task05: finite-state/frame-based relief-camp dialogue manager
- Task06: dialogue-act tagset and optional scikit-learn classifier
- Task07: content selection and discourse planning
- Task08: public/field-officer surface realisation
- Task09: toy IBM Model 1 EM, transfer/interlingua illustrations and unigram BLEU
- Task10: integrated pipeline and sanity tests
- Task11: design comparison and recommendation
- Task12: multi-party/noisy/code-mixed adaptation demonstration

## Run on Windows / VS Code
Open this folder in VS Code. Use the same Python interpreter for install and execution.
Most files use only the Python standard library. Task 6 optionally uses scikit-learn:
```powershell
python -m pip install scikit-learn
python Task06_Dialogue_Act_Classification.py
```
Run each task:
```powershell
python Task01_Discourse_Segmentation.py
python Task02_Reference_Resolution.py
python Task03_Text_Coherence.py
python Task04_Discourse_Structure.py
python Task05_Dialogue_Manager.py
python Task06_Dialogue_Act_Classification.py
python Task07_Discourse_Planning.py
python Task08_Surface_Realisation.py
python Task09_Machine_Translation.py
python Task10_Complete_Pipeline.py
python Task10_Test_Cases.py
python Task11_Design_Comparison.py
python Task12_Adapted_System.py
```
If `python` is not recognised, use your full Python executable path, for example:
```powershell
& "C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe" Task01_Discourse_Segmentation.py
```

## Important academic limitations
The assignment PDF specifies 1,200 reports / 40,000 tokens / 150 threads; 60 annotated reports and 400 referring expressions; 300 dialogues / 100 hand-tagged; 12 incident fields and 40 human-written bulletins; and 5,000 parallel sentence pairs per target language with 300 held out. This starter package contains only a small synthetic demonstration corpus. It does NOT meet those corpus sizes and does NOT provide a valid full-scale accuracy, BLEU or human-evaluation claim.
Some algorithms are intentionally simplified teaching baselines:
- Task 2 uses hand-supplied candidate trees, not a complete Hobbs parser.
- Task 3 uses heuristic entity roles.
- Task 4 uses discourse cue phrases, not a full RST parser.
- Task 6's tiny labels are for demonstration, not a held-out classifier benchmark.
- Task 9's toy parallel data and unigram BLEU are not standard translation evaluation.
Use these scripts to learn, run, capture outputs and extend with the required documented data and annotations. Do not report demo values as full-assignment results.

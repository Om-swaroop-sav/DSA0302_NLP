# DSA03 NLP Assignment 4 – Task-wise Python Codes

## Run
Install dependencies:
    python -m pip install -r requirements.txt
(Use the same Python interpreter selected in VS Code.)

Run complete demonstration:
    py Task10_Complete_Pipeline.py

Run tests:
    py Task10_Test_Cases.py

## Task-wise files
- Task03_FOPC_Knowledge_Base.py — FOPC facts, model checking and inference
- Task04_Named_Entity_Recognition.py — pension-domain NER baseline
- Task05_Syntax_Driven_Semantic_Analysis.py — semantic attachments and lambda reduction
- Task07_Word_Sense_Disambiguation.py — Lesk, MFS and supervised WSD
- Task08_Information_Retrieval.py — TF-IDF, inverted index and cosine ranking
- Task09_Annotation_Evaluation.py — raw agreement and Cohen's kappa
- Task10_Complete_Pipeline.py — integrated demonstration and plots
- Task10_Test_Cases.py — reproducibility checks
- Task12_Temporal_Pension_Rules.py — effective-date and service aggregation demo

Tasks 1, 2, 6 and 11 are primarily written/theoretical and do not need a separate standalone program in this code set.

## Dataset limitation
The included datasets are small synthetic demonstration data. They do not satisfy the assignment's minimum 300 circulars, 60,000 tokens, 200 enquiries, 600 hand-annotated sense occurrences and 60 relevance-judged queries. Replace/extend them with documented data and genuine annotations before reporting final experimental results. The NER component is a rule-based baseline.


Each task script now has a runnable demo block. Task 4, 5, 7, 8, 9 and 12 print sample results when run individually. Tasks 7, 8, 9 and 10 require scikit-learn; Task 10 also requires matplotlib.

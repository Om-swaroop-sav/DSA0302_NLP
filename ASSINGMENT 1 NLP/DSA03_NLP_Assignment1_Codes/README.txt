DSA03 - NATURAL LANGUAGE PROCESSING - ASSIGNMENT 1
Programming files

Files:
- task02_regex_entities.py
- task03_tokenization_normalization.py
- task04_nfa_to_dfa.py
- task07_morphological_analyser.py
- task08_orthographic_rules.py
- task09_porter_stemmer.py
- task09_stemming_vs_lemmatization.py
- task10_integrated_pipeline.py
- task12_ocr_correction.py
- task12_edit_distance.py
- task12_code_mixed_identifier.py
- task12_combined_processing.py

Requirements:
- Python 3
- NLTK (for Porter stemming and WordNet lemmatisation examples)

Install NLTK:
    python -m pip install nltk

Run a file:
    python task02_regex_entities.py

Run the integrated pipeline:
    python task10_integrated_pipeline.py

Notes:
1. These are educational starter implementations, not a clinically validated hospital system.
2. The FST example uses a small lookup relation; it is not a full 300-stem transducer.
3. The orthographic rules are simplified and need lexical/stress restrictions for production use.
4. OCR corrections should be context-verified. Do not automatically alter clinical values without review.
5. Actual assignment requirements still include 500 records, 25,000 tokens, 300 stems,
   40 clinician queries, 200 annotated word forms, full automata tables and measured evaluation.

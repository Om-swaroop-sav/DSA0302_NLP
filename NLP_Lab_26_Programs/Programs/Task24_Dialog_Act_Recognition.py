import re

utterances = [
    "Hello, good morning!",
    "Could you send the report, please?",
    "What time is the lab?",
    "Thank you for your help.",
    "Yes, I agree.",
    "Goodbye, see you tomorrow.",
    "The experiment starts at ten.",
]

def dialog_act(text):
    t = text.lower().strip()
    if re.search(r"\b(hello|hi|good morning|good evening)\b", t): return "GREETING"
    if re.search(r"\b(thank you|thanks)\b", t): return "THANKING"
    if re.search(r"\b(goodbye|bye|see you)\b", t): return "CLOSING"
    if re.search(r"\b(please|could you|would you|can you)\b", t): return "REQUEST"
    if t.endswith("?"): return "QUESTION"
    if re.match(r"^(yes|no|okay|ok|i agree)\b", t): return "CONFIRMATION"
    return "STATEMENT"

for utterance in utterances:
    print(f"{dialog_act(utterance):15} {utterance}")

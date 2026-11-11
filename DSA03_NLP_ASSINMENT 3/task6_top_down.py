"""Task 6: Top-down (recursive-descent) parser.
Run: python task6_top_down.py
This small grammar is a teaching/demo grammar for university helpdesk queries.
"""
import re

def tokenize(text):
    return re.findall(r"[A-Za-z]+|[0-9]+|[?.!,]", text.lower())


LEXICON = {
    "DET": {"the", "a", "an", "this", "that"},
    "N": {"student", "form", "timetable", "room", "library", "exam",
          "notice", "fee", "receipt", "hostel", "ticket"},
    "PRON": {"i", "you", "we", "they", "he", "she"},
    "NAME": {"om", "ajay"},
    "V": {"checks", "check", "submits", "submit", "books", "book",
          "starts", "start", "pays", "pay", "shows", "show"},
    "AUX": {"can", "could", "does", "do", "will"},
    "WH": {"when", "where", "what", "which", "who", "how"},
    "PREP": {"in", "on", "at", "near", "with", "for", "to", "from"},
}

class Parser:
    def __init__(self, words):
        self.words = words
        self.pos = 0

    def match(self, category):
        if self.pos < len(self.words) and self.words[self.pos] in LEXICON[category]:
            word = self.words[self.pos]
            self.pos += 1
            return (category, word)
        raise ValueError(f"Expected {category} at word {self.pos + 1}")

    def parse_np(self):
        start = self.pos
        try:
            if self.words[self.pos] in LEXICON["DET"]:
                det = self.match("DET")
                noun = self.match("N")
                return ("NP", det, noun)
            if self.words[self.pos] in LEXICON["PRON"]:
                return ("NP", self.match("PRON"))
            if self.words[self.pos] in LEXICON["NAME"]:
                return ("NP", self.match("NAME"))
        except (IndexError, ValueError):
            self.pos = start
            raise
        raise ValueError(f"Expected noun phrase at word {self.pos + 1}")

    def parse_pp(self):
        prep = self.match("PREP")
        np = self.parse_np()
        return ("PP", prep, np)

    def parse_vp(self):
        verb = self.match("V")
        children = [verb]
        if self.pos < len(self.words) and self.words[self.pos] in LEXICON["PREP"]:
            children.append(self.parse_pp())
        elif self.pos < len(self.words) and (
            self.words[self.pos] in LEXICON["DET"]
            or self.words[self.pos] in LEXICON["PRON"]
            or self.words[self.pos] in LEXICON["NAME"]
        ):
            children.append(self.parse_np())
            if self.pos < len(self.words) and self.words[self.pos] in LEXICON["PREP"]:
                children.append(self.parse_pp())
        return ("VP", *children)

    def parse(self):
        # Try a question with WH + AUX + NP + VP.
        start = self.pos
        try:
            if self.words[self.pos] in LEXICON["WH"]:
                wh = self.match("WH")
                aux = self.match("AUX")
                np = self.parse_np()
                vp = self.parse_vp()
                tree = ("S", wh, aux, np, vp)
            else:
                raise ValueError("Not a WH question")
        except (IndexError, ValueError):
            self.pos = start
            # Try AUX + NP + VP.
            try:
                aux = self.match("AUX")
                np = self.parse_np()
                vp = self.parse_vp()
                tree = ("S", aux, np, vp)
            except (IndexError, ValueError):
                self.pos = start
                # Try NP + VP, then imperative VP.
                try:
                    np = self.parse_np()
                    vp = self.parse_vp()
                    tree = ("S", np, vp)
                except (IndexError, ValueError):
                    self.pos = start
                    tree = ("S", self.parse_vp())
        if self.pos != len(self.words):
            raise ValueError(f"Unparsed words remain: {self.words[self.pos:]}")
        return tree

def show_tree(tree, level=0):
    if isinstance(tree, tuple):
        label = tree[0]
        print("  " * level + label)
        for child in tree[1:]:
            show_tree(child, level + 1)
    else:
        print("  " * level + str(tree))

if __name__ == "__main__":
    sentence = input("Enter a helpdesk sentence: ").strip()
    try:
        words = tokenize(sentence)
        tree = Parser(words).parse()
        print("\nSentence accepted. Parse tree:")
        show_tree(tree)
    except (ValueError, IndexError) as error:
        print("\nSentence rejected:", error)

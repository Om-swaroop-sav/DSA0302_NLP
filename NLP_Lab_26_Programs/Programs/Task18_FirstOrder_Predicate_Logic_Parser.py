import re

TOKEN = re.compile(r"\s*(forall|exists|->|<->|and|or|not|[A-Za-z_][A-Za-z_0-9]*|[(),])")

def tokenize(text):
    tokens, pos = [], 0
    while pos < len(text):
        match = TOKEN.match(text, pos)
        if not match:
            raise ValueError(f"Unexpected character at position {pos}: {text[pos]!r}")
        tokens.append(match.group(1))
        pos = match.end()
    return tokens

class Parser:
    def __init__(self, tokens): self.t, self.i = tokens, 0
    def peek(self): return self.t[self.i] if self.i < len(self.t) else None
    def take(self, expected=None):
        value = self.peek()
        if value is None or (expected and value != expected): raise ValueError(f"Expected {expected}, got {value}")
        self.i += 1
        return value
    def expression(self):
        left = self.disjunction()
        if self.peek() in ("->", "<->"):
            op = self.take(); right = self.expression(); return (op, left, right)
        return left
    def disjunction(self):
        node = self.conjunction()
        while self.peek() == "or": self.take(); node = ("or", node, self.conjunction())
        return node
    def conjunction(self):
        node = self.unary()
        while self.peek() == "and": self.take(); node = ("and", node, self.unary())
        return node
    def unary(self):
        if self.peek() == "not": self.take(); return ("not", self.unary())
        if self.peek() in ("forall", "exists"):
            quantifier = self.take(); variable = self.take(); return (quantifier, variable, self.unary())
        if self.peek() == "(":
            self.take(); node = self.expression(); self.take(")"); return node
        name = self.take()
        if self.peek() == "(":
            self.take(); args = [self.take()]
            while self.peek() == ",": self.take(); args.append(self.take())
            self.take(")"); return ("predicate", name, args)
        return ("symbol", name)

formula = "forall x (Human(x) -> Mortal(x))"
tokens = tokenize(formula)
parser = Parser(tokens)
ast = parser.expression()
if parser.peek() is not None: raise ValueError("Unexpected trailing tokens")
print("Formula:", formula)
print("Tokens:", tokens)
print("Parsed AST:", ast)

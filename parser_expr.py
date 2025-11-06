from ast_nodes import ASTNode
from symbols import add_if_not_exists

class ParserExpr:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected):
        tok = self.current()
        if tok and tok.lexeme == expected:
            self.pos += 1
            return
        raise Exception(f"Error: se esperaba '{expected}'")

    def parse(self):
        ast = self.E()
        return ast

    def E(self):
        left = self.T()
        return self.Ep(left)

    def Ep(self, inherited):
        tok = self.current()
        if tok and tok.lexeme in {"+", "-"}:
            op = tok.lexeme
            self.pos += 1
            right = self.T()
            node = ASTNode(op, inherited, right)
            return self.Ep(node)
        return inherited

    def T(self):
        left = self.F()
        return self.Tp(left)

    def Tp(self, inherited):
        tok = self.current()
        if tok and tok.lexeme in {"*", "/"}:
            op = tok.lexeme
            self.pos += 1
            right = self.F()
            node = ASTNode(op, inherited, right)
            return self.Tp(node)
        return inherited

    def F(self):
        tok = self.current()
        if tok.lexeme == "(":
            self.eat("(")
            node = self.E()
            self.eat(")")
            return node
        if tok.type == "NAME":
            add_if_not_exists(tok.lexeme)
            self.pos += 1
            return ASTNode("id", value=tok.lexeme)
        if tok.type == "NUMBER":
            self.pos += 1
            return ASTNode("num", value=float(tok.lexeme))
        raise Exception(f"Error: token inesperado '{tok.lexeme}' en F")

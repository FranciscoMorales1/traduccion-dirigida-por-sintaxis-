class ASTNode:
    def __init__(self, op, left=None, right=None, value=None):
        self.op = op
        self.left = left
        self.right = right
        self.value = value

    def print(self, level=0):
        indent = "    " * level
        if self.value is not None:
            print(f"{indent}{self.op}({self.value})")
        else:
            print(f"{indent}{self.op}")
            if self.left: self.left.print(level + 1)
            if self.right: self.right.print(level + 1)

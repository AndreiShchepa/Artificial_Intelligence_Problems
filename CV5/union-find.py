import re
import sys

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0


def parse_formula(formula_str):
    formula_str = formula_str.replace(" ", "")
    equalities = re.findall(r'\((\w+)=(\w+)\)', formula_str)
    inequalities = re.findall(r'\((\w+)!=(\w+)\)', formula_str)

    equalities = [(a, b) for a, b in equalities]
    inequalities = [(a, b) for a, b in inequalities]

    return equalities, inequalities


def is_satisfiable(formula_str):
    equations, inequalities = parse_formula(formula_str)
    uf = UnionFind()
    variables = set()

    for eq in equations + inequalities:
        variables.add(eq[0])
        variables.add(eq[1])

    for var in variables:
        uf.add(var)

    for a, b in equations:
        uf.union(a, b)

    for a, b in inequalities:
        if uf.find(a) == uf.find(b):
            return False

    return True


if len(sys.argv) < 2:
    formula = sys.stdin.read().strip()
else:
    formula = sys.argv[1]

print(formula)
print(f"Is the formula satisfiable? - {'Yes' if is_satisfiable(formula) else 'No'}")

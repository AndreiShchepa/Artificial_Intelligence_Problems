import random
import sys

def generate_random_formula(num_variables, num_clauses):
    if num_variables < 2:
        print("There must be at least 2 variables.")
        return None
    if num_clauses < 1:
        print("The number of clauses must be at least 1.")
        return None

    variables = [chr(ord('a') + i) for i in range(num_variables)]

    clauses = []
    for _ in range(num_clauses):
        var1, var2 = random.sample(variables, 2)
        operator = random.choice(["=", "!="])
        clauses.append(f"({var1} {operator} {var2})")

    formula = " ∧ ".join(clauses)
    return formula


if len(sys.argv) > 2:
    num_variables = int(sys.argv[1])
    num_clauses = int(sys.argv[2])
else:
    num_variables = int(input("Enter the number of variables: "))
    num_clauses = int(input("Enter the number of clauses: "))

max_pairs = num_variables * (num_variables - 1) // 2
if num_clauses > max_pairs:
    print(f"Too many clauses! The maximum number of unique clauses with {num_variables} variables is {max_pairs}.")
elif num_variables > 26:
    print(f"Too many variables! The maximum number of unique variables is 26.")
else:
    random_formula = generate_random_formula(num_variables, num_clauses)
    print(random_formula)

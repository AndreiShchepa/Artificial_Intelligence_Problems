import copy


def is_consistent(assignment, row, col):
    for c in range(col):
        if assignment[c] is None:
            continue

        if assignment[c] == row or abs(assignment[c] - row) == abs(c - col):
            return False

    return True


def revise(domain, Xi, Xj):
    revised = False

    # Iterate over domain[Xi] to avoid modification during iteration
    for x in domain[Xi][:]:
        if all(not is_consistent([x if k == Xi else None for k in range(len(domain))], y, Xj) for y in domain[Xj]):
            domain[Xi].remove(x)
            revised = True

    return revised


def ac3(variables, domain):
    queue = [(Xi, Xj) for Xi in variables for Xj in variables if Xi != Xj]
    while queue:
        Xi, Xj = queue.pop(0)
        if revise(domain, Xi, Xj):
            # If the domain of a variable is empty, no solution possible
            if not domain[Xi]:
                return False

            queue.extend((Xk, Xi) for Xk in variables if Xk != Xi)

    return True


def backtrack(assignment, variables, domain, all_solutions):
    if len(assignment) == len(variables):
        all_solutions.append(assignment)
        return

    col = len(assignment)
    for row in domain[col]:
        if not is_consistent(assignment, row, col):
            continue

        new_assignment = assignment + [row]
        new_domain = copy.deepcopy(domain)
        new_domain[col] = [row]

        if ac3(variables, new_domain):
            backtrack(new_assignment, variables, new_domain, all_solutions)


def is_symmetric(solution, all_solutions, n):
    def rotate_solution(solution, n):
        return [n - 1 - solution.index(i) for i in range(n)]

    def reflect_solution(solution, n):
        return [n - 1 - i for i in solution]


    rotations = [solution]
    for _ in range(3):
        rotations.append(rotate_solution(rotations[-1], n))

    reflections = [reflect_solution(rot, n) for rot in rotations]
    return any(rot in all_solutions for rot in rotations + reflections)


def n_queens_mgac_bt(n):
    variables = list(range(n))
    domain = {i: list(range(n)) for i in range(n)}

    all_solutions = []
    backtrack([], variables, domain, all_solutions)

    # Filter out symmetrical solutions to find fundamental solutions
    fundamental_solutions = []
    for solution in all_solutions:
        if not is_symmetric(solution, fundamental_solutions, n):
            fundamental_solutions.append(solution)

    return all_solutions, fundamental_solutions


for i in range(1, 11):
    n = i
    all_solutions, fundamental_solutions = n_queens_mgac_bt(n)

    print(f"{n}-Queens problem:")
    print(f"Total solutions found: {len(all_solutions)}")
    print(f"Fundamental solutions found: {len(fundamental_solutions)}\n")


import time
import sys


class Constraints:
    def __init__(self, sudoku):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if sudoku[i][j]!= 0:
                    self.__fill(i, j, sudoku[i][j])

    def __fill(self, i, j, num):
        self.rows[i].add(num)
        self.cols[j].add(num)
        self.squares[(i // 3) * 3 + (j // 3)].add(num)

    def do_move(self, i, j, num):
        self.__fill(i, j, num)

    def undo_move(self, i, j, num):
        self.rows[i].remove(num)
        self.cols[j].remove(num)
        self.squares[(i // 3) * 3 + (j // 3)].remove(num)

    def is_valid_move(self, i, j, num):
        return num not in self.rows[i] and num not in self.cols[j] and num not in self.squares[(i // 3) * 3 + (j // 3)]


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j

    return None


def optimized_backtracking_solver(grid, constraints):
    empty = find_empty(grid)
    if not empty:
        return grid

    row, col = empty
    for num in range(1, 10):
        if not constraints.is_valid_move(row, col, num):
            continue

        grid[row][col] = num
        constraints.do_move(row, col, num)
        if optimized_backtracking_solver(grid, constraints):
            return grid

        grid[row][col] = 0
        constraints.undo_move(row, col, num)

    return None


def backtracking_solver(grid, constraints):
    def is_valid_move(row, col, num):
        if num in grid[row]:
            return False

        for i in range(9):
            if grid[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False

        return True

    empty = find_empty(grid)
    if not empty:
        return grid

    row, col = empty
    for num in range(1, 10):
        if not is_valid_move(row, col, num):
            continue

        grid[row][col] = num

        if backtracking_solver(grid, constraints):
            return grid

        grid[row][col] = 0

    return None


def backjumping_solver(grid, constraints):
    def find_empty_fewest():
        best_count = 10
        best_pos = None

        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    valid_count = sum(1 for num in range(1, 10) if constraints.is_valid_move(i, j, num))
                    if valid_count < best_count:
                        best_count = valid_count
                        best_pos = (i, j)

                    # Dead end found, return immediately
                    if valid_count == 0:
                        return (i, j)
        return best_pos

    def get_conflicting_assignments(row, col, num):
        conflicts = set()

        for j in range(9):
            if j != col and grid[row][j] == num:
                conflicts.add((row, j))

        for i in range(9):
            if i != row and grid[i][col] == num:
                conflicts.add((i, col))

        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i != row or j != col) and grid[i][j] == num:
                    conflicts.add((i, j))

        return conflicts

    def backjump(level=0, prev_assignments=None):
        if prev_assignments is None:
            prev_assignments = set()

        pos = find_empty_fewest()
        if not pos:
            return True, set()  # Puzzle solved

        row, col = pos
        current_conflicts = set()

        for num in range(1, 10):
            if not constraints.is_valid_move(row, col, num):
                continue

            grid[row][col] = num
            constraints.do_move(row, col, num)

            current_pos = (row, col)
            current_assignments = prev_assignments | {current_pos}

            solved, conflicts = backjump(level + 1, current_assignments)

            if solved:
                return True, set()

            if conflicts:
                direct_conflicts = get_conflicting_assignments(row, col, num)

                # If current position caused conflict, remove current position from conflicts and add its direct conflicts
                if current_pos in conflicts:
                    conflicts.remove(current_pos)
                    conflicts.update(direct_conflicts & prev_assignments)

                current_conflicts.update(conflicts)

            # Undo move
            grid[row][col] = 0
            constraints.undo_move(row, col, num)

        if current_conflicts:
            # No value worked - return all accumulated conflicts plus current position
            return False, current_conflicts
        else:
            # Dead end - return all previous assignments as conflicts
            return False, prev_assignments

    solved, _ = backjump()
    return grid if solved else None


def load_sudokus(filename):
    sudokus = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace('.', '0')
            grid = [list(map(int, line[i:i+9])) for i in range(0, 81, 9)]
            sudokus.append(grid)

    return sudokus


def measure_performance_backtracking_simpler(sudokus):
    algorithms = {
        "Backtracking": backtracking_solver,
        "Optimized Backtracking": optimized_backtracking_solver,
        "Backjumping": backjumping_solver,
    }

    for name, solver in algorithms.items():
        start_time = time.time()
        solved_count = 0
        for sudoku in sudokus:
            grid_copy = [row[:] for row in sudoku]
            constraints = Constraints(grid_copy)

            if solver(grid_copy, constraints):
                solved_count += 1

        end_time = time.time()
        print(f"{name:<25} solved {solved_count:<7} out of {len(sudokus):<8} {end_time - start_time:<10.4f}")


if __name__ == "__main__":
    print(f"{'':<6}{'Method':<17} {'Solved Count':<15} {'Total Puzzles':<15} {'Time (s)':<10}")
    print("-" * 66)
    measure_performance_backtracking_simpler(load_sudokus(sys.argv[1]))
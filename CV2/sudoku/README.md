# Sudoku Solver Implementation

This project implements three different algorithms for solving Sudoku puzzles: basic backtracking, optimized backtracking, and backjumping.
Each algorithm offers different performance characteristics and solving strategies.

## Constraints Management

The `Constraints` class maintains the state of the Sudoku board by tracking numbers present in:
- Rows (9 sets, one for each row)
- Columns (9 sets, one for each column)
- 3x3 Squares (9 sets, one for each square)

## Algorithm Implementations

### 1. Basic Backtracking
The simplest implementation that uses a depth-first search approach.

How it works:
1. Find the first empty cell (0)
2. Try numbers 1-9 in that cell
3. For each number:
   - Check if it's valid (not in same row, column, or 3x3 square)
   - If valid, place the number and recursively solve the rest
   - If the recursive call fails, undo the move and try the next number
4. If no number works, backtrack to the previous cell

Advantages:
- Simple implementation
- Low memory usage

Disadvantages:
- Checks constraints repeatedly
- No optimization for reducing backtracks

### 2. Optimized Backtracking
Similar to basic backtracking but uses the `Constraints` class to improve performance.

Key improvements:
- Maintains sets of used numbers for quick constraint checking
- Avoids repeated scanning of rows, columns, and squares
- Faster constraint validation through set operations

But there is still lack of optimization for reducing backtracks.

### 3. Backjumping
The most sophisticated implementation that includes intelligent backtracking and conflict detection.

Key features:
- Identifies the source of conflicts
- Jumps back multiple levels when a dead end is found
- Uses forward checking to detect dead ends early

Detailed implementation:

1. **Smart Cell Selection:**
   - Instead of choosing the first empty cell, it finds the cell with the fewest valid options
   - This reduces the branching factor of the search
   - Immediately identifies dead ends where no valid options exist

2. **Conflict Tracking:**
   - When a dead end is reached, it identifies which previous assignments caused the conflict
   - Creates a "conflict set" containing the positions that led to the failure
   - Allows skipping back multiple levels to the source of the conflict

3. **Intelligent Backtracking:**
   - Instead of backing up one level at a time, it can jump back multiple levels
   - Only backtracks to relevant assignments that could resolve the conflict
   - Maintains conflict information to avoid repeating the same dead ends

## Results of tests

| Method | Solved Count | Total Puzzles | Time (min) |
|--------|--------------|---------------|------------|
| Backtracking | 95 | 95 | 30.9 |
| Optimized Backtracking | 95 | 95 | 23.5 |
| Backjumping | 95 | 95 | 1.75 |
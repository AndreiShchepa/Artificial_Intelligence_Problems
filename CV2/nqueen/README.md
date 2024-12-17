# N-Queens Solver Implementation

This project implements different approaches to solve the N-Queens puzzle using CSP (Constraint Satisfaction Problem) techniques, backtracking, and symmetry handling. The implementation includes MAC (Maintaining Arc Consistency) with backtracking and comprehensive symmetry detection.

## The N-Queens Problem

The N-Queens puzzle requires placing **N** chess queens on an N×N chessboard so that no two queens threaten each other. This means:
- No two queens can share the same row
- No two queens can share the same column
- No two queens can share the same diagonal

## Core Components

### 1. Arc Consistency (AC-3 Algorithm)

The AC-3 algorithm maintains arc consistency by:
1. Creating a queue of all variable pairs
2. Revising domains based on constraints
3. If a domain is revised, adding affected variables back to the queue
4. Continuing until no more revisions are possible

### 2. Backtracking with MAC

The backtracking algorithm:
1. Checks if assignment is complete
2. For each unassigned variable (column):
   - Tries each value in its domain
   - Checks consistency
   - Maintains arc consistency
   - Recursively continues search
   - Backtracks if necessary

### 3. Symmetry Handling
Symmetry handling involves generating all symmetrical variants through:
   - 90-degree rotations (4 variants)
   - Reflections (2 variants for each rotation)

### 4. Variables, Domain, and Constraints

- **Variables**:
   - Each column of the board (0 to n-1)
   - This representation automatically ensures no two queens share a column

- **Domain**:
   - For each variable: possible row positions (0 to n-1)
   - Initially, each queen can be placed in any row

- **Constraints**:
   - Row constraint: No two queens in the same row
   - Diagonal constraint: No two queens on the same diagonal
   - Column constraint: No two queens on the same column (implicitly in the implementation)
   

## Performance Notes

The implementation uses several optimization techniques:
1. MAC (Maintaining Arc Consistency) to prune search space early
2. Domain copying to maintain state during backtracking
3. Early consistency checking to avoid unnecessary exploration

## Results

---

***1**-Queens problem:*
Total solutions found: 1
Fundamental solutions found: 1

---

***2**-Queens problem:*
Total solutions found: 0
Fundamental solutions found: 0

---

***3**-Queens problem:*
Total solutions found: 0
Fundamental solutions found: 0

---

***4**-Queens problem:*
Total solutions found: 2
Fundamental solutions found: 1

---

***5**-Queens problem:*
Total solutions found: 10
Fundamental solutions found: 2

---

***6**-Queens problem:*
Total solutions found: 4
Fundamental solutions found: 1

---

***7**-Queens problem:*
Total solutions found: 40
Fundamental solutions found: 6

---

***8**-Queens problem:*
Total solutions found: 92
Fundamental solutions found: 12

---

***9**-Queens problem:*
Total solutions found: 352
Fundamental solutions found: 46

---

***10**-Queens problem:*
Total solutions found: 724
Fundamental solutions found: 92

---

Computation for more queens takes a lot of time, so there should be space for some improvements.
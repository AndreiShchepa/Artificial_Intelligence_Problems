## 1. Formula Generator (formula-generator.py)
Generates random logical formulas for testing the satisfiability checker.

### Usage
```bash
python3 formula-generator.py <num_variables> <num_clauses>
```

## 2. Union-Find Satisfiability Checker (union-find.py)
Checks the satisfiability of a formula consisting of equalities 
and inequalities using the **Union-Find** (Disjoint Set Union) data structure.

### Usage
```bash
python3 formula-generator.py <num_variables> <num_clauses> | python3 union-find.py
```

### Complexity Analysis:
- Time Complexity:
**O(nlog*n)**, where `n` is the number of variables. This complexity arises due 
to path compression and union by rank optimizations in the Union-Find structure.
    - https://en.wikipedia.org/wiki/Ackermann_function
    - https://www.geeksforgeeks.org/union-by-rank-and-path-compression-in-union-find-algorithm/

- Space Complexity: 
**O(n)** for storing parent and rank information for each variable.

## 3. Examples
```bash
python3 formula-generator.py 7 5 | python3 union-find.py 
(a = f) ∧ (e != d) ∧ (c != f) ∧ (f != g) ∧ (a != d)
Is the formula satisfiable? - Yes
```

```bash
python3 formula-generator.py 5 4 | python3 union-find.py 
(a = b) ∧ (c != d) ∧ (c = a) ∧ (b != c)
Is the formula satisfiable? - No
```
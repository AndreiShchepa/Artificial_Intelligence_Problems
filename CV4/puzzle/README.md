# Puzzle
https://en.wikipedia.org/wiki/15_puzzle

## Prerequisites
```bash
git clone https://github.com/aibasel/downward.git
cd downward
./build.py
```

## Usage
```bash
./fast-downward.py <domain.pddl> <problem.pddl> --search "astar(lmcut())"
```
OR
```bash
./fast-downward.py --alias seq-sat-lama-2011 <domain.pddl> <problem.pddl>
```

## Results
### Puzzle-8
```bash
./fast-downward.py --alias seq-sat-lama-2011 puzzle/domain.pddl puzzle/puzzle-8.pddl
```

[t=0.014898s, 10492 KB] Solution found!\
[t=0.014917s, 10492 KB] Actual search time: 0.002225s\
slide n3 c32 c22\
slide n1 c33 c32\
slide n6 c23 c33\
slide n3 c22 c23\
slide n5 c21 c22\
slide n7 c11 c21\
slide n2 c12 c11\
slide n4 c13 c12\
slide n3 c23 c13\
slide n5 c22 c23\
slide n1 c32 c22\
slide n8 c31 c32\
slide n7 c21 c31\
slide n1 c22 c21\
slide n4 c12 c22\
slide n2 c11 c12\
slide n1 c21 c11\
slide n4 c22 c21\
slide n5 c23 c22\
slide n6 c33 c23\
[t=0.015044s, 10492 KB] Plan length: 20 step(s).


### Puzzle-15
```bash
./fast-downward.py --alias seq-sat-lama-2011 puzzle/domain.pddl puzzle/puzzle-15.pddl
```

[t=42.802285s, 180588 KB] Solution found!\
[t=42.802373s, 180588 KB] Actual search time: 22.670764s\
slide n6 c33 c23\
slide n14 c32 c33\
slide n13 c22 c32\
slide n6 c23 c22\
slide n12 c24 c23\
slide n15 c14 c24\
slide n4 c13 c14\
slide n11 c12 c13\
slide n3 c11 c12\
slide n1 c21 c11\
slide n7 c31 c21\
slide n13 c32 c31\
slide n9 c42 c32\
slide n8 c41 c42\
slide n13 c31 c41\
slide n9 c32 c31\
slide n8 c42 c32\
slide n5 c43 c42\
slide n14 c33 c43\
slide n2 c34 c33\
slide n15 c24 c34\
slide n12 c23 c24\
slide n2 c33 c23\
slide n8 c32 c33\
slide n6 c22 c32\
slide n2 c23 c22\
slide n8 c33 c23\
slide n14 c43 c33\
slide n10 c44 c43\
slide n15 c34 c44\
slide n12 c24 c34\
slide n8 c23 c24\
slide n11 c13 c23\
slide n3 c12 c13\
slide n2 c22 c12\
slide n7 c21 c22\
slide n9 c31 c21\
slide n6 c32 c31\
slide n5 c42 c32\
slide n10 c43 c42\
slide n14 c33 c43\
slide n11 c23 c33\
slide n7 c22 c23\
slide n5 c32 c22\
slide n6 c31 c32\
slide n9 c21 c31\
slide n5 c22 c21\
slide n6 c32 c22\
slide n10 c42 c32\
slide n14 c43 c42\
slide n15 c44 c43\
[t=42.802657s, 180588 KB] Plan length: 51 step(s).


# Robot with Obstacles Algorithm Project Report

## Problem Statement

Consider a vacuum cleaner world, i.e., a regular square grid where each cell is either empty or contains dirt or obstacle. Furthermore, an automatic vacuum cleaner moves in this environment, always located on one of the grid cells. The vacuum cleaner can move to an adjacent cell or it can vacuum, resulting in an empty cell where the vacuum cleaner is located.

### 1. Grid Representation
The environment is represented as a 2D grid (matrix), where each cell can take one of three values:
  - 0: Empty cell where the vacuum cleaner can move.
  - 1: Trash that needs to be cleaned.
  - -1: Obstacle where the vacuum cleaner cannot move.
### 2. Vacuum Actions
  - The vacuum cleaner starts at a specified position on the grid.
  - The vacuum can move to adjacent cells (up, down, left, right) as long as the cell is not an obstacle (-1).
  - When the vacuum reaches a cell containing trash (1), it can clean it, leaving the cell empty (0).
### 3. Goal
The vacuum cleaner must clean all the trash on the grid while taking the shortest possible path. The algorithms are responsible for determining the optimal sequence of actions (movements and cleaning operations) to achieve this goal.

## Solution Description

### 1. Breadth-First Search (BFS)

BFS explores all possible paths level by level. It always explores the shortest path first, making it a guaranteed optimal algorithm for this grid problem. 
`Trade-off` - it guarantees finding the shortest path, but may use more memory exploring all nodes on the certain depth.

### 2. Depth-First Search (DFS)

DFS explores paths by diving deeper into one branch of the search tree before backtracking.
`Trade-off` - it is memory-efficient (`linear space complexity`), but can not guarantee finding the shortest path.

### 3. A* Search

A* uses both the actual cost to reach a state `g(x)` and a heuristic estimate of the cost to the goal `h(x)`. The heuristic used in this implementation is the `Manhattan distance to the nearest trash cell`.

#### 3.1 Heuristic Function
```python
def heuristic(self, position, trash_positions):
    return min(abs(position[0] - t[0]) + abs(position[1] - t[1]) for t in trash_positions) if trash_positions else 0
```
The heuristic calculates the `Manhattan distance` from the vacuum's current position to the nearest trash cell, helping A* prioritize paths that seem closer to the goal.

## Results
This program demonstrates the use of BFS, DFS, and A* to solve the vacuum cleaning problem on a grid with obstacles. Each algorithm has different characteristics in terms of efficiency and optimality:

  - **BFS** guarantees the shortest path but may be slower for large grids.
  - **DFS** is memory-efficient but does not guarantee the shortest path.
  - **A*** combines the advantages of both, using a heuristic to guide the search toward the goal efficiently while still guaranteeing the shortest path because of `admissible` heuritic.

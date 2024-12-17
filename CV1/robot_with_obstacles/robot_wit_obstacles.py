from collections import deque
import heapq


class VacuumCleaner:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.trash_positions = self.find_trash_positions()

    def find_trash_positions(self):
        trash = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1:  # 1 means trash, 0 means empty
                    trash.append((r, c))
        return trash

    def get_neighbors(self, position):
        r, c = position
        neighbors = []

        # Check if each neighbor is within bounds and not an obstacle (-1)
        if r > 0 and self.grid[r - 1][c] != -1: neighbors.append((r - 1, c))  # up
        if r < self.rows - 1 and self.grid[r + 1][c] != -1: neighbors.append((r + 1, c))  # down
        if c > 0 and self.grid[r][c - 1] != -1: neighbors.append((r, c - 1))  # left
        if c < self.cols - 1 and self.grid[r][c + 1] != -1: neighbors.append((r, c + 1))  # right
        return neighbors

    def is_goal_state(self, trash_positions):
        return len(trash_positions) == 0

    def bfs(self):
        start_state = (self.start, tuple(self.trash_positions))  # (position, remaining_trash)
        queue = deque([(start_state, [])])  # (state, actions)
        visited = {start_state}

        while queue:
            (position, trash_positions), actions = queue.popleft()
            if self.is_goal_state(trash_positions):
                return actions

            # Move to neighbors
            for neighbor in self.get_neighbors(position):
                new_state = (neighbor, trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + ['MOVE', neighbor]))

            # Clean the current position
            if position in trash_positions:
                new_trash_positions = tuple(t for t in trash_positions if t != position)
                new_state = (position, new_trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + ['CLEAN']))

        return None

    def dfs(self, max_depth=100):
        start_state = (self.start, tuple(self.trash_positions))  # (position, remaining_trash)
        stack = [(start_state, [], 0)]  # (state, actions, current_depth)
        visited = {start_state}

        while stack:
            (position, trash_positions), actions, depth = stack.pop()

            if depth > max_depth:
                continue

            if self.is_goal_state(trash_positions):
                return actions

            # Move to neighbors
            for neighbor in self.get_neighbors(position):
                new_state = (neighbor, trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    stack.append((new_state, actions + ['MOVE', neighbor], depth + 1))

            # Clean the current position
            if position in trash_positions:
                new_trash_positions = tuple(t for t in trash_positions if t != position)
                new_state = (position, new_trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    stack.append((new_state, actions + ['CLEAN'], depth + 1))

        return None

    # Heuristic for A* - Manhattan distance
    def heuristic(self, position, trash_positions):
        return min(abs(position[0] - t[0]) + abs(position[1] - t[1]) for t in trash_positions) if trash_positions else 0

    def a_star(self):
        start_state = (self.start, tuple(self.trash_positions))  # (position, remaining_trash)
        priority_queue = [
            (self.heuristic(self.start, self.trash_positions), start_state, [])]  # (heuristic + cost, state, actions)
        visited = {start_state}

        while priority_queue:
            _, (position, trash_positions), actions = heapq.heappop(priority_queue)
            if self.is_goal_state(trash_positions):
                return actions

            # Move to neighbors
            for neighbor in self.get_neighbors(position):
                new_state = (neighbor, trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    new_cost = len(actions) + 1
                    heapq.heappush(priority_queue, (
                    new_cost + self.heuristic(neighbor, trash_positions), new_state, actions + ['MOVE', neighbor]))

            # Clean the current position
            if position in trash_positions:
                new_trash_positions = tuple(t for t in trash_positions if t != position)
                new_state = (position, new_trash_positions)
                if new_state not in visited:
                    visited.add(new_state)
                    new_cost = len(actions) + 1
                    heapq.heappush(priority_queue, (
                    new_cost + self.heuristic(position, new_trash_positions), new_state, actions + ['CLEAN']))

        return None


def print_actions(actions, name_alg):
    print(f"{name_alg} Plan:")
    if not actions:
        print("No actions to display.")
        return

    print("-" * 30)

    step = 1
    i = 0
    while i < len(actions):
        action = actions[i]

        if action == "MOVE":
            position = actions[i + 1]
            print(f"Step {step}: Move to position {position}.")
            i += 2

        elif action == "CLEAN":
            print(f"Step {step}: Clean the current position.")
            i += 1

        step += 1

    print("-" * 30)
    print(f"Total actions: {step - 1}")

# 0 - empty, 1 - trash, -1 - obstacle
grid = [
    [0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0],
    [0,   0,   1,   0,   0],
    [0,   0,   0,   0,   0],
    [0,  -1,  -1,  -1,   0],
    [0,  -1,   1,  -1,   0],
    [0,  -1,   0,  -1,   0],
    [0,  -1,   0,   0,   0],
    [0,   0,   0,   1,   0]
]

vacuum = VacuumCleaner(grid, (0, 0))

print_actions(vacuum.bfs(), 'BFS')
print('\n################################\n')
print_actions(vacuum.dfs(), 'DFS')
print('\n################################\n')
print_actions(vacuum.a_star(), 'A*')
from collections import deque

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_new_states(current, blank_pos):
    x, y = blank_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_states = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            new_state = [row[:] for row in current]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            new_states.append(new_state)

    return new_states

def bfs(initial, goal):
    visited = set()
    queue = deque([(initial, [])])
    visited.add(tuple(map(tuple, initial)))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal:
            return path

        blank_pos = find_blank(current_state)
        new_states = generate_new_states(current_state, blank_pos)

        for state in new_states:
            state_tuple = tuple(map(tuple, state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((state, path + [state]))

    return None

def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()

if __name__ == "__main__":
    initial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    solution = bfs(initial, goal)

    if solution:
        print("Solution found!\n")
        print_path(solution)
    else:
        print("No solution exists.")
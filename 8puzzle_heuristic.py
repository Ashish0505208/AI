import heapq

def tiles_out_of_place(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    x, y = divmod(blank_index, 3)

    moves = {
        "UP": (x - 1, y),
        "DOWN": (x + 1, y),
        "LEFT": (x, y - 1),
        "RIGHT": (x, y + 1),
    }

    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: tiles_out_of_place(start, goal)}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            return True

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            h_score = tiles_out_of_place(neighbor, goal)
            f_score_neighbor = tentative_g_score + h_score

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = f_score_neighbor
                heapq.heappush(priority_queue, (f_score_neighbor, neighbor))

                print("State:")
                for row in range(0, 9, 3):
                    print(neighbor[row:row+3])
                print(f"h(n) = {h_score}, g(n) = {tentative_g_score}, f(n) = {f_score_neighbor}\n")

    return False

def get_puzzle_state(prompt):
    print(prompt)
    state = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (space-separated, use 0 for blank tile): ").split()
        state.extend([int(num) for num in row])
    return tuple(state)

if __name__ == "__main__":
    print("\nProvide the initial state as a 3x3 grid:")
    use_default = input("Do you want to use a default initial state? (yes/no): ").strip().lower()

    if use_default == "yes":
        start_state = (1, 2, 3, 4, 5, 6, 7,0, 8)
        print("Using default initial state:")
        for row in range(0, 9, 3):
            print(start_state[row:row+3])
        goal_state=(1,2,3,4,5,6,7,8,0)
        print("Using a default goal state")
        for row in range(0,9,3):
            print(goal_state[row:row+3])
    else:
        start_state = get_puzzle_state("Enter the initial state:")
        goal_state = get_puzzle_state("Enter the goal state:")

    if a_star(start_state, goal_state):
        print("\nSolution found!")
    else:
        print("\nNo solution exists.")
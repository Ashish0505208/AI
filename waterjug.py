from collections import deque

# Function to get user input for jug capacities and goal state
def get_user_input():
    capacities = {}
    for i in range(1, 4):
        while True:
            try:
                capacities[f'jug{i}'] = int(input(f"Enter the capacity of Jug {i}: "))
                if capacities[f'jug{i}'] <= 0:
                    raise ValueError("Capacity must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a positive integer.")
    
    while True:
        try:
            goal_state = int(input("Enter the desired final state (any one jug's water level): "))
            if goal_state < 0 or goal_state > max(capacities.values()):
                raise ValueError("Goal state must be within the range of the jug capacities.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    return capacities, goal_state

# Function to check if the goal state is reached
def is_goal_state(state, goal_state):
    return goal_state in state

# Function to pour water from one jug to another
def pour(state, from_jug, to_jug, capacities):
    J1, J2, J3 = state
    if from_jug == 'jug1' and to_jug == 'jug2':
        transfer = min(J1, capacities['jug2'] - J2)
        NJ1, NJ2, NJ3 = J1 - transfer, J2 + transfer, J3
    elif from_jug == 'jug1' and to_jug == 'jug3':
        transfer = min(J1, capacities['jug3'] - J3)
        NJ1, NJ2, NJ3 = J1 - transfer, J2, J3 + transfer
    elif from_jug == 'jug2' and to_jug == 'jug3':
        transfer = min(J2, capacities['jug3'] - J3)
        NJ1, NJ2, NJ3 = J1, J2 - transfer, J3 + transfer
    elif from_jug == 'jug2' and to_jug == 'jug1':
        transfer = min(J2, capacities['jug1'] - J1)
        NJ1, NJ2, NJ3 = J1 + transfer, J2 - transfer, J3
    elif from_jug == 'jug3' and to_jug == 'jug1':
        transfer = min(J3, capacities['jug1'] - J1)
        NJ1, NJ2, NJ3 = J1 + transfer, J2, J3 - transfer
    elif from_jug == 'jug3' and to_jug == 'jug2':
        transfer = min(J3, capacities['jug2'] - J2)
        NJ1, NJ2, NJ3 = J1, J2 + transfer, J3 - transfer
    return (NJ1, NJ2, NJ3)

# Breadth-first search implementation
def bfs(start_state, capacities, goal_state):
    queue = deque([[start_state]])  # Start with a list containing the initial state
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]  # Get the last state in the current path

        print(f"Exploring state: {state}")  # Debug statement

        if is_goal_state(state, goal_state):
            print("\nSolution:")
            for i, step in enumerate(path):
                print(f"Step {i + 1}: {step}")
            return

        for from_jug in capacities:
            for to_jug in capacities:
                if from_jug != to_jug:
                    next_state = pour(state, from_jug, to_jug, capacities)
                    if next_state not in visited:
                        print(f"Adding state: {next_state}")  # Debug statement
                        visited.add(next_state)
                        queue.append(path + [next_state])  # Add new state to the path

    print("No solution found.")  # If BFS exhausts without a solution

# Main code
if __name__ == "__main__":
    capacities, goal_state = get_user_input()
    start_state = (capacities['jug1'], 0, 0)  # Assuming Jug 1 is initially full
    bfs(start_state, capacities, goal_state)

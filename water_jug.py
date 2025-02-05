# from collections import deque

# # Define the capacities of the jugs
# capacities = {
#     'jug1': 8,
#     'jug2': 5,
#     'jug3': 3
# }

# # Function to check if the goal state is reached
# def is_goal_state(state):
#     return 4 in state

# # Function to pour water from one jug to another
# def pour(state, from_jug, to_jug):
#     J1, J2, J3 = state
#     if from_jug == 'jug1' and to_jug == 'jug2':
#         transfer = min(J1, capacities['jug2'] - J2)
#         NJ1 = J1 - transfer
#         NJ2 = J2 + transfer
#         NJ3 = J3
#     elif from_jug == 'jug1' and to_jug == 'jug3':
#         transfer = min(J1, capacities['jug3'] - J3)
#         NJ1 = J1 - transfer
#         NJ3 = J3 + transfer
#         NJ2 = J2
#     elif from_jug == 'jug2' and to_jug == 'jug3':
#         transfer = min(J2, capacities['jug3'] - J3)
#         NJ2 = J2 - transfer
#         NJ3 = J3 + transfer
#         NJ1 = J1
#     elif from_jug == 'jug2' and to_jug == 'jug1':
#         transfer = min(J2, capacities['jug1'] - J1)
#         NJ2 = J2 - transfer
#         NJ1 = J1 + transfer
#         NJ3 = J3
#     elif from_jug == 'jug3' and to_jug == 'jug1':
#         transfer = min(J3, capacities['jug1'] - J1)
#         NJ3 = J3 - transfer
#         NJ1 = J1 + transfer
#         NJ2 = J2
#     elif from_jug == 'jug3' and to_jug == 'jug2':
#         transfer = min(J3, capacities['jug2'] - J2)
#         NJ3 = J3 - transfer
#         NJ2 = J2 + transfer
#         NJ1 = J1
#     return (NJ1, NJ2, NJ3)

# # Breadth-first search implementation
# def bfs(start_state):
#     queue = deque([[start_state]])  # Start with a list containing the initial state
#     visited = set()

#     while queue:
#         path = queue.popleft()
#         state = path[-1]  # Get the last state in the current path

#         print(f"Exploring state: {state}")  # Debug statement

#         if is_goal_state(state):
#             print("Solution:")
#             for i, step in enumerate(path):
#                 print(f"Rule {i + 1}: {step}")
#             return

#         for from_jug in capacities:
#             for to_jug in capacities:
#                 if from_jug != to_jug:
#                     next_state = pour(state, from_jug, to_jug)
#                     if next_state not in visited:
#                         print(f"Adding state: {next_state}")  # Debug statement
#                         visited.add(next_state)
#                         queue.append(path + [next_state])  # Add new state to the path

#     print("No solution found.")  # If BFS exhausts without a solution

# # Initial state
# start_state = (8, 0, 0)

# # Solve the problem
# bfs(start_state)









from collections import deque
capacities = {'jug1': 8, 'jug2': 5, 'jug3': 3}
goal_state=int(input("Enter goal state: "))
def is_goal_state(state):
    return goal_state in state
jug_indices = {'jug1': 0, 'jug2': 1, 'jug3': 2}
def pour(state, from_jug, to_jug):
    J1, J2, J3 = state
    from_index = jug_indices[from_jug]
    to_index = jug_indices[to_jug]
    transfer = min(state[from_index], capacities[to_jug] - state[to_index])
    next_state = list(state)
    next_state[from_index] -= transfer
    next_state[to_index] += transfer
    return tuple(next_state)
def bfs(start_state):
    queue, visited = deque([[start_state]]), set()
    while queue:
        path = queue.popleft()
        state = path[-1]
        if is_goal_state(state):
            print("Solution:")
            for i, step in enumerate(path):
                print(f"Rule {i + 1}: {step}")
            return
        for from_jug, to_jug in [(i, j) for i in capacities for j in capacities if i != j]:
            next_state = pour(state, from_jug, to_jug)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(path + [next_state])
    print("No solution found.")
bfs((8, 0, 0))
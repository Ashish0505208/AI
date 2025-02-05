import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue for the frontier (cost, node, path)
    frontier = [(0, start, [start])]
    explored = set()

    while frontier:
        # Pop the node with the lowest cost
        cost, current_node, path = heapq.heappop(frontier)

        # If the goal is reached, return the path and cost
        if current_node == goal:
            return path, cost

        # Mark the current node as explored
        if current_node in explored:
            continue
        explored.add(current_node)

        # Add neighbors to the frontier
        for neighbor, weight in graph[current_node]:
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')  # If no path is found

def get_user_input():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    print("Enter the neighbors and costs for each node in the format: neighbor cost")
    print("Type 'done' when you finish entering neighbors for a node.")

    for _ in range(n):
        node = input("Enter node name: ")
        graph[node] = []
        while True:
            entry = input(f"Enter neighbor and cost for node {node} (or 'done'): ")
            if entry.lower() == 'done':
                break
            neighbor, cost = entry.split()
            graph[node].append((neighbor, int(cost)))

    return graph

if __name__ == "__main__":
    # Get the graph input from the user
    graph = get_user_input()

    # Get start and goal nodes
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    path, cost = uniform_cost_search(graph, start, goal)

    if path:
        print(f"Shortest path: {' -> '.join(path)} with total cost: {cost}")
    else:
        print("No path found.")










# import heapq
# def uniform_cost_search(graph, start, goal):
#     frontier = [(0, start, [start])]
#     explored = set()
#     while frontier:
#         cost, node, path = heapq.heappop(frontier)
#         if node == goal:
#             return path, cost
#         if node in explored:
#             continue
#         explored.add(node)
#         for neighbor, weight in graph[node]:
#             if neighbor not in explored:
#                 heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))
#     return None, float('inf')
# def get_user_input():
#     graph = {}
#     for _ in range(int(input("Enter the number of nodes: "))):
#         node = input("Enter node name: ")
#         graph[node] = []
#         while (entry := input(f"Enter neighbor and cost for {node} (or 'done'): ")) != 'done':
#             neighbor, cost = entry.split()
#             graph[node].append((neighbor, int(cost)))
#     return graph
# if __name__ == "__main__":
#     graph = get_user_input()
#     start, goal = input("Enter the start node: "), input("Enter the goal node: ")
#     path, cost = uniform_cost_search(graph, start, goal)
#     print(f"Shortest path: {' -> '.join(path)} with total cost: {cost}" if path else "No path found.")
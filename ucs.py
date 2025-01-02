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

if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'C': [('B', 2), ('T', 1), ('O', 3), ('E', 5), ('P', 5)],
        'B': [('A', 1), ('R', 4), ('S', 3)],
        'T': [],
        'O': [('I', 2), ('N', 5)],
        'E': [('G', 5)],
        'P': [('L', 5), ('F', 1), ('D', 3)],
        'A': [],
        'R': [],
        'S': [],
        'I': [('Z', 2)],
        'N': [],
        'G': [],
        'L': [],
        'F': [],
        'D': [],
        'Z': []
    }

    start = 'C'
    goal = 'Z'

    path, cost = uniform_cost_search(graph, start, goal)

    if path:
        print(f"Shortest path: {' -> '.join(path)} with total cost: {cost}")
    else:
        print("No path found.")
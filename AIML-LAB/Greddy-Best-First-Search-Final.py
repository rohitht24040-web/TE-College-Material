import heapq
import time

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}


def greedy_best_first_search(start, goal):

    priority_queue = []
    visited = set()
    nodes_explored = 0

    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    while priority_queue:

        h, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return path, nodes_explored

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    return None, nodes_explored


def find_cost(path):

    cost = 0

    for i in range(len(path) - 1):
        for neighbor, edge_cost in graph[path[i]]:
            if neighbor == path[i + 1]:
                cost += edge_cost

    return cost


start_time = time.perf_counter()

path, nodes = greedy_best_first_search('A', 'G')

end_time = time.perf_counter()

execution_time = end_time - start_time


print("Greedy Best First Search")

if path:
    print("Path:", " -> ".join(path))
    print("Path Cost:", find_cost(path))
    print("Nodes Explored:", nodes)
    print("Execution Time:", execution_time, "seconds")
else:
    print("No path found")
    
    

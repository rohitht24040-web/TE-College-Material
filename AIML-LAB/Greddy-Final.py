import heapq
import time

graph = {
    'A': [('B', 1), ('C', 1), ('D', 1)],
    'B': [('E', 1), ('F', 1)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0
}


def greedy_best_first_search(start, goal):

    visited = set()
    priority_queue = []
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


start_time = time.perf_counter()

path, nodes = greedy_best_first_search('A', 'G')

end_time = time.perf_counter()

execution_time = end_time - start_time


if path:
    cost = 0

    for i in range(len(path) - 1):
        for neighbor, edge_cost in graph[path[i]]:
            if neighbor == path[i + 1]:
                cost += edge_cost
                break

    print("Greedy Best First Search")
    print("Path:", " -> ".join(path))
    print("Path Cost:", cost)
    print("Nodes Explored:", nodes)
    print("Execution Time:", execution_time, "seconds")
else:
    print("No path found")

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


def a_star_search(start, goal):

    visited = set()
    priority_queue = []
    nodes_explored = 0

    heapq.heappush(
        priority_queue,
        (heuristic[start], 0, start, [start])
    )

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return path, g, nodes_explored

        for neighbor, cost in graph[current]:

            if neighbor not in visited:

                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, 0, nodes_explored


start_time = time.perf_counter()

path, cost, nodes = a_star_search('A', 'G')

end_time = time.perf_counter()

execution_time = end_time - start_time


if path:

    print("A* Search")
    print("Path:", " -> ".join(path))
    print("Path Cost:", cost)
    print("Nodes Explored:", nodes)
    print("Execution Time:", f"{execution_time:.2f}", "seconds")

else:
    print("No path found")

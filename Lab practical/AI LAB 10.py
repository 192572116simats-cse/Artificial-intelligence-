import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 3)],
    'D': [('G', 3)],
    'G': []
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'G': 0
}

def astar(start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    print("A* SEARCH ALGORITHM")
    print("-------------------")
    print("Starting Node:", start)
    print("Goal Node:", goal)
    print("\nSearching for the shortest path...\n")

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print("Current Node:", current)
        print("Path:", " -> ".join(path))
        print("Path Cost (g):", g)
        print("Heuristic (h):", heuristic[current])
        print("Total Cost (f = g + h):", f)
        print()

        if current == goal:
            print("GOAL REACHED!")
            print("Shortest Path:", " -> ".join(path))
            print("Minimum Path Cost:", g)
            return

        for neighbour, cost in graph[current]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    print("Goal cannot be reached.")


astar('S', 'G')

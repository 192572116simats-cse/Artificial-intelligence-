from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BREADTH-FIRST SEARCH")
    print("--------------------")
    print("Starting Node:", start)
    print("\nTraversal Order:")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print("Visited:", node)
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    print("\nFinal BFS Traversal:", " -> ".join(visited_order))

visited_order = []

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited_order.clear()

    print("BREADTH-FIRST SEARCH")
    print("--------------------")
    print("Starting Node:", start)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            visited_order.append(node)

            print("Visited Node:", node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    print("\nFinal BFS Traversal:", " -> ".join(visited_order))


bfs(graph, 'A')

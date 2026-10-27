graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)

        print("Visited Node:", node)

        for neighbour in graph[node]:
            dfs(neighbour)


print("DEPTH-FIRST SEARCH")
print("------------------")
print("Starting Node: A")
print("\nTraversal Order:")

dfs('A')

print("\nFinal DFS Traversal:", " -> ".join(visited))

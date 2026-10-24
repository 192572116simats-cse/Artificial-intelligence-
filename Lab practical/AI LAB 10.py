from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
best = float('inf')

for route in permutations(cities):
    path = (0,) + route + (0,)
    cost = sum(dist[path[i]][path[i+1]]
               for i in range(len(path)-1))

    if cost < best:
        best = cost
        best_path = path

print("Best route:", best_path)
print("Minimum distance:", best)

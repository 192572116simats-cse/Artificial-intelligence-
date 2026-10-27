from itertools import permutations

cities = ['A', 'B', 'C', 'D']

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
other_cities = [1, 2, 3]

minimum_cost = float('inf')
best_route = []

print("TRAVELLING SALESMAN PROBLEM")
print("---------------------------")
print("Cities:", cities)
print("Starting City: A")
print("\nPossible Tours:")

for route in permutations(other_cities):
    tour = (start,) + route + (start,)
    cost = 0

    for i in range(len(tour) - 1):
        cost += distance[tour[i]][tour[i + 1]]

    route_names = [cities[i] for i in tour]

    print(" -> ".join(route_names), "| Cost:", cost)

    if cost < minimum_cost:
        minimum_cost = cost
        best_route = route_names

print("\nOPTIMAL TOUR")
print("------------")
print("Best Route:", " -> ".join(best_route))
print("Minimum Travel Cost:", minimum_cost)

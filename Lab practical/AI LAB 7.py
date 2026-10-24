rooms = {'A': 1, 'B': 1}
position = 'A'

while True:
    if rooms[position] == 1:
        print("Cleaning", position)
        rooms[position] = 0

    if position == 'A':
        position = 'B'
    else:
        break

print("All rooms cleaned")

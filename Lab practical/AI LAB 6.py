rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

print("VACUUM CLEANER PROBLEM")
print("----------------------")
print("Initial Room Status:", rooms)
print("Vacuum Cleaner starts at Room", location)

while 'Dirty' in rooms.values():

    print("\nVacuum Cleaner is in Room", location)

    if rooms[location] == 'Dirty':
        print("Room", location, "is Dirty")
        print("Action: Suck")
        rooms[location] = 'Clean'
        print("Room", location, "is now Clean")

    else:
        print("Room", location, "is already Clean")

    if location == 'A':
        location = 'B'
    else:
        location = 'A'

print("\nFINAL ROOM STATUS")
print("-----------------")
print("Room A:", rooms['A'])
print("Room B:", rooms['B'])
print("All rooms are Clean.")
print("Vacuum Cleaner has completed its task.")

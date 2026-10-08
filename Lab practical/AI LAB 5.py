from collections import deque

def safe(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    mr = 3 - m
    cr = 3 - c

    if mr > 0 and mr < cr:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    moves = [
        (1, 0), (2, 0),
        (0, 1), (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if safe(new_state[0], new_state[1]):
                queue.append((new_state, path))


solve()

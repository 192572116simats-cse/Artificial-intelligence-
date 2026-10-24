from collections import deque

def solve():
    q = deque([((3, 3, 1), [])])
    visited = set()

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))
        path = path + [(m, c, b)]

        if (m, c, b) == (0, 0, 0):
            for state in path:
                print(state)
            return

        for x, y in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            nm = m - x if b else m + x
            nc = c - y if b else c + y

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (nm == 3 or 3-nm >= 3-nc):
                    q.append(((nm, nc, 1-b), path))

solve()

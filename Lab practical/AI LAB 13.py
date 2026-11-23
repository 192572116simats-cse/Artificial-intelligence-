# Minimax Algorithm

def minimax(depth, node, is_max):
    if depth == 2:
        return node

    if is_max:
        return max(
            minimax(depth + 1, node * 2, False),
            minimax(depth + 1, node * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True),
            minimax(depth + 1, node * 2 + 1, True)
        )

result = minimax(0, 3, True)

print("Best value using Minimax:", result)

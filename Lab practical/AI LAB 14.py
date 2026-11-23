

def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 2:
        return node

    if is_max:
        best = float('-inf')

        for i in [node * 2, node * 2 + 1]:
            value = alphabeta(depth + 1, i, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in [node * 2, node * 2 + 1]:
            value = alphabeta(depth + 1, i, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

result = alphabeta(0, 3, float('-inf'), float('inf'), True)

print("Best value using Alpha-Beta Pruning:", result)

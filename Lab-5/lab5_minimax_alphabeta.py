import math

scores = [3, 5, 2, 9, 3, 5, 2, 9]
tree_depth = int(math.log2(len(scores)))

minimax_leaves = 0
alphabeta_leaves = 0


def minimax(depth, index, is_max):
    global minimax_leaves
    if depth == tree_depth:
        minimax_leaves = minimax_leaves + 1
        return scores[index]
    if is_max:
        return max(minimax(depth + 1, index * 2, False),
                   minimax(depth + 1, index * 2 + 1, False))
    else:
        return min(minimax(depth + 1, index * 2, True),
                   minimax(depth + 1, index * 2 + 1, True))


def alphabeta(depth, index, is_max, alpha, beta):
    global alphabeta_leaves
    if depth == tree_depth:
        alphabeta_leaves = alphabeta_leaves + 1
        return scores[index]
    if is_max:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


print("Lab 5: Minimax and Alpha-Beta Pruning")
print("Leaf scores:", scores)
print("Tree depth:", tree_depth)
print()

left_value = minimax(1, 0, False)
right_value = minimax(1, 1, False)
minimax_leaves = 0
print("Value of left move:", left_value)
print("Value of right move:", right_value)
print()

value1 = minimax(0, 0, True)
print("Minimax optimal value:", value1)
print("Leaves checked by minimax:", minimax_leaves)

value2 = alphabeta(0, 0, True, float("-inf"), float("inf"))
print("Alpha-beta optimal value:", value2)
print("Leaves checked by alpha-beta:", alphabeta_leaves)
print()

scores = [9, 2, 5, 3, 9, 2, 5, 3]
minimax_leaves = 0
alphabeta_leaves = 0
print("Reordered leaf scores:", scores)
value3 = minimax(0, 0, True)
print("Minimax optimal value:", value3)
print("Leaves checked by minimax:", minimax_leaves)
value4 = alphabeta(0, 0, True, float("-inf"), float("inf"))
print("Alpha-beta optimal value:", value4)
print("Leaves checked by alpha-beta:", alphabeta_leaves)
print()
print("The value stays the same in both orders, only the leaf count of alpha-beta changes.")

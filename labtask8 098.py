import math
def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
def is_board_full(board):
    return all(board[i][j] != 0 for i in range(3) for j in range(3))
def min_max(board, depth, is_maximizing):
    if check_winner(board, 1): return 10 - depth
    if check_winner(board, -1): return depth - 10
    if is_board_full(board): return 0
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = max(best, min_max(board, depth + 1, False))
                    board[i][j] = 0
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = min(best, min_max(board, depth + 1, True))
                    board[i][j] = 0
        return best
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                move_val = min_max(board, 0, False)
                board[i][j] = 0
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move
board = [
    [1, -1, 1],
    [0, -1, 0],
    [1, 0, 0]
]
best_move = find_best_move(board)
print(f"Best move for AI: Row {best_move[0]}, Column {best_move[1]}")

import math
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
def create_board():
    return [[EMPTY] * 3 for _ in range(3)]
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)
def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if is_full(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
        return best_score
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
def play_game():
    board = create_board()
    print_board(board)
    while True:
        while True:
            row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                break
            print("Invalid move, try again.")
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        print("AI's move:")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = PLAYER_X
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break
if __name__ == "__main__":
    play_game()
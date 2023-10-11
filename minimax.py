import time

# Initialize the game board as a 5x6 grid
board = [[' ' for _ in range(6)] for _ in range(5)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 19)

# Function to check if a player has won
def check_win(player, board):
    for i in range(5):
        for j in range(6):
            if (j < 3 and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == player) or \
               (i < 2 and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == player) or \
               (i < 2 and j < 3 and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == player) or \
               (i < 2 and j > 2 and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == player):
                return True
    return False

# Function to evaluate a state using the heuristic
def evaluate_state(player, board):
    h = 0
    for i in range(5):
        for j in range(6):
            if board[i][j] == player:
                # Check for potential 4-in-a-row
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        consecutive = 0
                        for k in range(1, 4):
                            x, y = i + k * dx, j + k * dy
                            if 0 <= x < 5 and 0 <= y < 6 and board[x][y] == player:
                                consecutive += 1
                            else:
                                break
                        if consecutive == 2:
                            h += 200
                        elif consecutive == 1:
                            h += 150
                # Check for potential 3-in-a-row
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        consecutive = 0
                        for k in range(1, 3):
                            x, y = i + k * dx, j + k * dy
                            if 0 <= x < 5 and 0 <= y < 6 and board[x][y] == player:
                                consecutive += 1
                            else:
                                break
                        if consecutive == 1:
                            h += 20
    return h

# Function to implement the minimax algorithm with alpha-beta pruning
def minimax(board, depth, player, alpha, beta):
    if depth == 0 or check_win('x', board) or check_win('o', board):
        return evaluate_state('o', board) - evaluate_state('x', board)
    
    if player == 'o':
        max_eval = float('-inf')
        for i in range(5):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = 'o'
                    eval = minimax(board, depth - 1, 'x', alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(5):
            for j in range(6):
                if board[i][j] == ' ':
                    board[i][j] = 'x'
                    eval = minimax(board, depth - 1, 'o', alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the player
def find_best_move(board, depth, player):
    best_eval = float('-inf') if player == 'o' else float('inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for i in range(5):
        for j in range(6):
            if board[i][j] == ' ':
                board[i][j] = player
                eval = minimax(board, depth - 1, 'x' if player == 'o' else 'o', alpha, beta)
                board[i][j] = ' '
                if (player == 'o' and eval > best_eval) or (player == 'x' and eval < best_eval):
                    best_eval = eval
                    best_move = (i, j)
                if player == 'o':
                    alpha = max(alpha, eval)
                else:
                    beta = min(beta, eval)
    return best_move

# Player 1's initial move
board[3][4] = 'x'
print_board(board)

# Player 2's initial move
board[3][3] = 'o'
print_board(board)

# Continue the game
for move in range(12):
    if move % 2 == 0:
        # Player 1's turn
        start_time = time.time()
        best_move = find_best_move(board, 2, 'x')
        end_time = time.time()
        board[best_move[0]][best_move[1]] = 'x'
        print(f"Player 1: {best_move} - {end_time - start_time:.5f} sec")
    else:
        # Player 2's turn
        start_time = time.time()
        best_move = find_best_move(board, 4, 'o')
        end_time = time.time()
        board[best_move[0]][best_move[1]] = 'o'
        print(f"Player 2: {best_move} - {end_time - start_time:.5f} sec")
    print_board(board)

# Check the result
if check_win('x', board):
    print("Player 1 (X) wins!")
elif check_win('o', board):
    print("Player 2 (O) wins!")
else:
    print("It's a tie!")

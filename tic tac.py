import math

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def evaluate(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return 1 if row[0] == 'X' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 1 if board[0][col] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 1 if board[0][0] == 'X' else -1

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 1 if board[0][2] == 'X' else -1

    # No winner
    return 0

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                cells.append((i, j))
    return cells

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1:
        return score - depth
    elif score == -1:
        return score + depth
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = 'X'
            score = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = 'O'
            score = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = 'X'
        score = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        if is_full(board) or evaluate(board) != 0:
            break
        row = int(input('Enter the row number (0-2): '))
        col = int(input('Enter the column number (0-2): '))
        if board[row][col] == ' ':
            board[row][col] = 'O'

            if is_full(board) or evaluate(board) != 0:
                break

            # AI player's turn
            best_move = get_best_move(board)
            board[best_move[0]][best_move[1]] = 'X'
        else:
            print('Invalid move. Try again.')

    print_board(board)
    score = evaluate(board)
    if score == 1:
        print("AI wins!")
    elif score == -1:
        print("Human wins!")
    else:
        print("It's a tie!")

play()

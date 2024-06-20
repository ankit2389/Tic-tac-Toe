import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player_mark in [X, O]:
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(board[i][j] == player_mark for j in range(3)) or all(board[j][i] == player_mark for j in range(3)):
                return player_mark
        if all(board[i][i] == player_mark for i in range(3)) or all(board[i][2 - i] == player_mark for i in range(3)):
            return player_mark
    return None

def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        max_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > max_value:
                max_value = value
                best_action = action
        return best_action
    else:
        min_val = math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value < min_val:
                min_val = value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

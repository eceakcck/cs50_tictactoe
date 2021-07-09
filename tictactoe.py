"""
Tic Tac Toe Player
"""

import math
import copy

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
    
    Count num of empty's in set. modulo 2.
    == 0 -->> O's turn.
    == 1 -->> 1's turn.
    """
    n=0
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                n = n+1
    
    if (n % 2) == 0:
        return O
    if (n % 2) == 1:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    checks the whole board.
    takes the location of emptys 
    adds to tuple
    """
    
    possible_set=set(())
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                move_tuple = (i,j,)
                possible_set.add(move_tuple)
        
    return possible_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    
    takes board, tuple -->> if not suitable action -->> raise an error
    
    DONT update the given board. Return a new one.
    """
    
    new_board = copy.deepcopy(board)
        
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
        
    else:
        raise Exception("Not Valid")
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    make a set of X locations.
    make a set of Y locations.
    
    check if either of them contain one of the "win" states.
    """
    
    win1={(0,0),(0,1),(0,2)}
    win2={(1,0),(1,1),(1,2)}
    win3={(2,0),(2,1),(2,2)}
    win4={(0,0),(1,0),(2,0)} 
    win5={(0,1),(1,1),(2,1)}
    win6={(0,2),(1,2),(2,2)}
    win7={(0,0),(1,1),(2,2)}
    win8={(0,2),(1,1),(2,0)}
    
    x_set=set(())
    o_set=set(())
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                loc_tuple = (i,j,)
                x_set.add(loc_tuple)
            if board[i][j] == O:
                loc_tuple = (i,j,)
                o_set.add(loc_tuple)
    
    if win1.issubset(x_set) or win2.issubset(x_set) or win3.issubset(x_set) or win4.issubset(x_set) or win5.issubset(x_set) or win6.issubset(x_set) or win7.issubset(x_set) or win8.issubset(x_set):
        return X
    elif win1.issubset(o_set) or win2.issubset(o_set) or win3.issubset(o_set) or win4.issubset(o_set) or win5.issubset(o_set) or win6.issubset(o_set) or win7.issubset(o_set) or win8.issubset(o_set):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    if someone won -> game is over
    if no empty holes left -> game is over
    
    else -->> FALSE
    """
    """winner(board) == None or"""
    
    if (EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]) or winner(board) == X or winner(board) == O:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == None:
        return 0
    
def max_value(board):
    """
    This function will take a board as input state
    and return the action that will lead to the result with the highest terminal value
    """
    if terminal(board):
        return utility(board)
    else:
        v=-100
        for action in actions(board):
            v=max(v, min_value(result(board, action)))
        
        return v

def min_value(board):
    """
    This function will take a board as input state
    and return the action that will lead to the result with the lowest terminal value
    """
    if terminal(board):
        return utility(board)
    else:
        v=100
        for action in actions(board):
            v=min(v, max_value(result(board, action)))
        
        return v
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    ALFA BETA PRUNING?
    """
    act = (-1, -1)
    
    if terminal(board):
        return None
    if player(board) == X:
        """X will try to MAXIMIZE the outcome"""
        v = -100
        for action in actions(board):
            t = min_value(result(board, action))
            if t >= v:
                v = t
                act = action
                
            
    if player(board) == O:
        """O will try to MINIMIZE the outcome"""
        v = 100
        for action in actions(board):
            t = max_value(result(board,action))
            if t <= v:
                v = t
                act = action
        
    return act
            
    
    
    
    

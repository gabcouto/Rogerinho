import random
import sys
from typing import Tuple

from advsearch.othello.gamestate import GameState

DEPTH = 7

def evaluate(state: GameState):
    valor = 0
    ############################################
    board = state.get_board()
    for i in range(8):
        for j in range(8):
            if board.tiles[i][j] == 'B':
                valor+=1 #para cada peça preta
                # +3 para cada canto, +1 para cada peça na parede, +2 para cada antes do canto
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    valor += 3
                elif i == 0 or i == 7 or j == 0 or j == 7:
                    valor += 1
                elif (i == 6 or i == 1) and (j == 1 or j ==6):
                    valor += 2

            elif board.tiles[i][j] == 'W':
                valor -= 1
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    valor -= 3
                elif i == 0 or i == 7 or j == 0 or j == 7:
                    valor -= 1
                if (i == 1 or i ==6) and (j == 1 or j ==6 ):
                    valor -= 2

            else:
                if(board.is_legal((i,j), 'B')):
                    valor += 2
                if(board.is_legal((i,j), 'W')):
                    valor -= 2
    
    if state.player == 'B':
        return valor
    else:
        return -(valor)


def max_player(state: GameState, alpha, beta, depth) -> Tuple[int, int, int]:
    depth+=1
    if (depth == DEPTH or state.is_terminal()):
        return (evaluate(state), (-1, -1))

    v = -(sys.maxsize)
    act = (-1, -1)
    for action in state.legal_moves():

        val_act = min_player(state.next_state(action), alpha, beta, depth)
        v = max(v, val_act[0])
        act = action
        alpha = max(alpha, v)
        if (beta<=alpha): break

    return (alpha, act)


def min_player(state: GameState, alpha, beta, depth) -> Tuple[int, int, int]:
    depth+=1
    if (depth == DEPTH or state.is_terminal()):
        return (evaluate(state), (-1, -1))

    v = sys.maxsize
    act = (-1, -1)
    for action in state.legal_moves():

        val_act = max_player(state.next_state(action), alpha, beta, depth)
        v = min(v, val_act[0])
        act =  action
        beta = min(beta, v)
    
        if (beta<=alpha): break

    return (beta, act)


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    value, move = max_player(state, sys.maxsize, -sys.maxsize, 0)
    return move
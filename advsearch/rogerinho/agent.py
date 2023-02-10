import random
import sys
from typing import Tuple

from ..othello.gamestate import GameState

DEPTH = 6

def evaluate(state: GameState):
    
    valor = 0

    for i in range(8):
        for j in range(8):
            if state[i][j] == 'B':
                valor+=1 #para cada peça preta
                # +3 para cada canto, +1 para cada peça na parede, +2 para cada antes do canto
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    valor += 3
                elif i == 0 or i == 7 or j == 0 or j == 7:
                    valor += 1
                elif (i == 6 or i == 1) and (j == 1 or j ==6):
                    valor += 2

            elif state[i][j] == 'W':
                valor -= 1
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    valor -= 3
                elif i == 0 or i == 7 or j == 0 or j == 7:
                    valor -= 1
                if (i == 1 or i ==6) and (j == 1 or j ==6 ):
                    valor -= 2

    ############################################## Não sei como implementar isso na real
    # Delta quantidade de opções de jogadas
    #black_moves = 0
    #white_moves = 0
    #for i in range(8):
     #   for j in range(8):
      #      if state[i][j] == '.':
       #         if is_legal_move(state, i, j): #como verifica se é legal para o preto e n pro branco?
        #            black_moves += 1
         #       if is_legal_move(state, i, j):
          #          white_moves += 1

    #valor += (black_moves - white_moves) * 2
    ############################################
    
    # if (somos pretas):
    return valor
    #else
    #return -(valor)


def max_player(state: GameState, alpha, beta, depth) -> Tuple[int, int, int]:
    depth+=1
    if (depth == DEPTH or state.is_terminal):
        return (evaluate(state), (-1, -1))

    v = -(sys.maxsize)
    act = None
    for action in state.legal_moves:

        val_act = min_player(state.next_state(action), alpha, beta)
        v = max(v, val_act[0])
        if v > alpha :
            act = action
            alpha = v
    
        if (beta<=alpha): break

    return (alpha, action)


def min_player(state: GameState, alpha, beta, depth) -> Tuple[int, int, int]:
    depth+=1
    if (depth == DEPTH or state.is_terminal):
        return (evaluate(state), (-1, -1))

    v = sys.maxsize
    act = None
    for action in state.legal_moves:

        val_act = max_player(state.next_state(action), alpha, beta)
        v = min(v, val_act[0])
        if v < beta :
            act = action
            beta = v
    
        if (beta<=alpha): break

    return (beta, action)


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """



    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


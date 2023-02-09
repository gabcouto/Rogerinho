import random
import sys
from typing import Tuple

from ..othello.gamestate import GameState

def try_cut(state: Gamestate):

def evaluate(state: Gamestate):

def successors(state: Gamestate):

def max_player(state: Gamestate, alpha, beta) -> Tuple[int, int, int]:
    if try_cut(state):
        return evaluate(state)
    current = -sys.maxsize
    action = None
    for sbar, abar in successors(state):
        min_tuple = min_player(sbar, alpha, beta)
        current = max(current, min_tuple[0])
        action = abar
        alpha = max(alpha, current)
        if(alpha >= beta):
            break
    return alpha, action

def min_player(state: Gamestate, alpha, beta) -> Tuple[int, int, int]:
    if try_cut(state):
        return evaluate(state)
    current = sys.maxsize
    action = None
    for sbar, abar in successors(state):
        max_tuple = max_player(sbar, alpha, beta)
        current = min(current, max_tuple[0])
        action = abar
        beta = min(beta, current)
        if(alpha >= beta):
            break
    return beta, action

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """



    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


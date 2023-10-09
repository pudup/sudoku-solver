from copy import deepcopy
from board_gen import gen_board


def generateBoards():
    board = gen_board()
    always_unsolved = deepcopy(board)
    user_board = deepcopy(board)

    return board, user_board, always_unsolved

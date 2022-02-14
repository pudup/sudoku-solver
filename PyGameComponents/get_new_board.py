import requests
from copy import deepcopy

def generateBoards():
    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    board = response.json()["board"]
    always_unsolved = deepcopy(board)
    user_board = deepcopy(board)

    return board, user_board, always_unsolved

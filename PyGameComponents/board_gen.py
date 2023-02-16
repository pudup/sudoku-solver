import random
from solverUIHelp import helperfunc


def gen_board():
    grid = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    main_options = [1,2,3,4,5,6,7,8,9]

    for _ in range(17):
        yay = False
        while not yay:
            posisX = random.randint(0, 8)
            posisY = random.randint(0, 8)

            if grid[posisX][posisY] == 0:
                yay = True
                options = []
                for i in main_options:
                    options.append(i)
                while options:
                    choice = random.choice(options)
                    if helperfunc(choice, posisX, posisY, grid):
                        grid[posisX][posisY] = choice
                    else:
                        options.remove(choice)
    return grid
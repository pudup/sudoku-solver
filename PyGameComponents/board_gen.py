import random
from solverUIHelp import helperfunc, sudoku_solver

count = 0


def sudoku_solver_count(grid):
    global count
    for i in range(0, 9):  # Loop through X positions
        for j in range(0, 9):  # Loop through Y positions
            if grid[i][j] == 0:  # Check if position is empty
                for k in range(1, 10):  # Try all numbers in empty position using helper function
                    if helperfunc(number=k, position_x=i, position_y=j, grid=grid):
                        grid[i][j] = k  # If true then set position to working number
                        sudoku_solver_count(grid)  # Recurse
                        grid[i][j] = 0  # If dead end then reset

                return False  # Return when dead end
    count += 1
    return False


def gen_board():
    global count
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(14):
        seed = random.randint(1, 9)
        seedposX = random.randint(0, 8)
        seedposY = random.randint(0, 8)
        if grid[seedposX][seedposY] == 0 and helperfunc(seed, seedposX, seedposY, grid):
            grid[seedposX][seedposY] = seed
    sudoku_solver(grid)

    tried_posis = []
    for i in range(75):
        tryX = random.randint(0, 8)
        tryY = random.randint(0, 8)
        if [tryX, tryY] in tried_posis:
            continue
        else:
            tried_posis.append([tryX, tryY])
        count = 0
        old = grid[tryX][tryY]
        grid[tryX][tryY] = 0
        sudoku_solver_count(grid)
        if count != 1:
            grid[tryX][tryY] = old
    return grid

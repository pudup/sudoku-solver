import os
from time import sleep, time
import sys

mega_hard_grid = [
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 1, 8],
    [0, 0, 0, 0, 8, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 3, 0, 0],
]

easy_grid = [
    [0, 3, 0, 0, 9, 0, 0, 0, 8],
    [4, 0, 0, 1, 5, 0, 6, 0, 9],
    [8, 0, 9, 0, 0, 3, 0, 5, 0],
    [0, 0, 0, 0, 3, 7, 9, 2, 0],
    [7, 5, 0, 0, 0, 9, 0, 0, 0],
    [2, 9, 0, 4, 1, 0, 0, 8, 5],
    [5, 0, 8, 0, 4, 0, 1, 7, 0],
    [0, 0, 7, 3, 0, 0, 0, 6, 4],
    [3, 0, 1, 6, 0, 5, 0, 0, 0],
]

try:
    visualizeYN = sys.argv[1]
    visualizeYN = float(visualizeYN)
    if visualizeYN == 0:
        print(f"Solving without visual")
    else:
        print(f"Using visual speed of {visualizeYN} seconds")
    sleep(2.5)
    doit = True
except:
    doit = False
    print("Using default no visual. Provide argument as a number, e.g. 0.05 for visual")

try:
    if sys.argv[2] == "hard":
        grid_to_use = mega_hard_grid
        print("Using very hard grid")
    else:
        grid_to_use = easy_grid
        print("Using default easy grid")
except:
    grid_to_use = easy_grid
    print("Using default easy grid")


def pretty_matrix(array):
    for count, i in enumerate(array):
        line = ""
        if count == 3 or count == 6:
            for _ in range(len(i) + 2):
                line += "-" + " "
            print(line)
            line = ""
        for count, value in enumerate(i):
            if value == 0:
                value = "_"
            if count == 2 or count == 5:
                line += str(value) + " "
                line += "|" + " "
            else:
                line += str(value) + " "
        print(line)


def helperfunc(number, position_x, position_y, grid):  # Return true if number works in position on grid, else false
    x = position_x
    y = position_y

    for i in range(0, 9):  # Checks if number exists in row
        if grid[x][i] == number:
            return False
    for i in range(0, 9):  # Checks if number exists in column
        if grid[i][y] == number:
            return False
    for i in range(0, 3):  # Checks if number exists in the box
        for j in range(0, 3):
            if grid[((x // 3) * 3) + i][((y // 3) * 3) + j] == number:
                return False
    return True


def sudoku_solver(grid, visual=0.0):
    start = time()
    for i in range(0, 9):  # Loop through X positions
        for j in range(0, 9):  # Loop through Y positions
            if grid[i][j] == 0:  # Check if position is empty
                for k in range(1, 10):  # Try all numbers in empty position using helper function
                    if helperfunc(number=k, position_x=i, position_y=j, grid=grid):
                        grid[i][j] = k  # If true then set position to working number
                        if visual:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            pretty_matrix(grid)
                            sleep(visual)
                        can_continue = sudoku_solver(grid, visual)  # Recurse
                        if can_continue:
                            return True

                        grid[i][j] = 0  # If dead end then reset
                return False  # Return when no 0s in grid

    print("\n")
    pretty_matrix(grid)  # Print a working solution
    end = time()
    print("\n" + "Solved in " + str(end - start) + " seconds")
    more = input("\nY/N for more solutions: ")
    # Currently seems to go on forever if given grid only has one solution when Y is chosen
    # Comment above is not entirely true. Easy grids immediately return with no more solutions.
    if more.lower() == "y":
        return False
    else:
        return True


if __name__ == "__main__":
    if doit:
        sudoku_solver(grid_to_use, visualizeYN)
    else:
        sudoku_solver(grid_to_use, )


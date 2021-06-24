import numpy
example_grid = [[0, 0, 0, 8, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 4, 3],
                [5, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 7, 0, 8, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 2, 0, 0, 3, 0, 0, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 7, 5],
                [8, 0, 3, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 6, 0, 0],]







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
            if grid[((x // 3) * 3)+i][((y // 3) * 3)+j] == number:
                # print("False")
                return False
    return True



def sudoku_solver(grid):
    for i in range(0, 9):  # Loop through X positions
        for j in range(0, 9): # Loop through Y positions
            if grid[i][j] == 0:  # Check if position is empty
                for k in range(1, 10):  # Try all numbers in empty position using helper function
                    if helperfunc(number=k, position_x=i, position_y=j, grid=grid):
                        grid[i][j] = k  # If true then set position to working number
                        sudoku_solver(grid)  # Recurse
                        grid[i][j] = 0  # If dead end then reset
                return  # Return when no 0s in grid


    print(numpy.matrix(grid))  # Print a working solution
    more = input("Y/N for more solutions: ")
    if more.lower() == "y":
        pass
    else:
        exit()


sudoku_solver(example_grid)
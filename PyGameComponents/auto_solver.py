from solverUIHelp import helperfunc
from time import sleep
from colours_and_fonts import *
import pygame

background_col = BACKGROUND_COL
thin_lines_col = THIN_LINES_COL
thicc_lines_col = THICC_LINES_COL
numbers_col = NUMBERS_COL


def solve_board(window, board, always_unsolved, ):
    for i in range(0, 9):  # Loop through X positions
        for j in range(0, 9):  # Loop through Y positions
            if board[i][j] == 0:  # Check if position is empty
                for k in range(1, 10):  # Try all numbers in empty position using helper function
                    if helperfunc(number=k, position_x=i, position_y=j, grid=board):
                        board[i][j] = k  # If true then set position to working number
                        solver_redraw(window, board, always_unsolved, )
                        highlight_square(window, (i + 1, j + 1))
                        pygame.display.update()
                        sleep(0.05)
                        can_continue = solve_board(window, board, always_unsolved, )  # Recurse
                        if can_continue:
                            return True

                        board[i][j] = 0  # If dead end then reset
                return False  # Return when no 0s in grid

    return True


def solver_redraw(window, board, always_unsolved, ):
    font = pygame.font.SysFont("Verdana", 64)
    window.fill(background_col)  # Clear screen
    for i in range(10):  # Can be written in one loop if using a single colour
        if i % 3 != 0:  # Remove unnecessary lines
            pygame.draw.line(window, thin_lines_col, (80 + (80 * i), 80), (80 + (80 * i), 800), 2)
            pygame.draw.line(window, thin_lines_col, (80, 80 + (80 * i)), (800, 80 + (80 * i)), 2)
    for i in range(
            10):  # Extra loop written to avoid thin lines being drawn over thick lines (visually less attractive)
        if i % 3 == 0:
            pygame.draw.line(window, thicc_lines_col, (80 + (80 * i), 80), (80 + (80 * i), 801),
                             4)  # 801 to smoothen corner
            pygame.draw.line(window, thicc_lines_col, (80, 80 + (80 * i)), (801, 80 + (80 * i)), 4)
    for y in range(0, len(board[0])):
        for x in range(0, len(board[0])):
            if board[y][x] != always_unsolved[y][x]:
                num = font.render(str(board[y][x]), True, (24, 29, 49))
                window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
            elif board[y][x] != 0:
                num = font.render(str(board[y][x]), True, numbers_col)
                window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
    pygame.display.update()


def highlight_square(window, position):
    x, y = position[1], position[0]
    for i in range(2):
        pygame.draw.line(window, (193, 222, 174), ((i * 80) + x * 80, y * 80), ((i * 80) + x * 80, y * 80 + 80), 8)
        pygame.draw.line(window, (193, 222, 174), (x * 80, (i * 80) + y * 80), (x * 80 + 80, (i * 80) + y * 80), 8)
        pygame.display.update()

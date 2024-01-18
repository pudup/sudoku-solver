import pygame
from colours_and_fonts import *
from solverUIHelp import helperfunc


def add_a_num(window, position, event, user_board, Y, X):
    font = pygame.font.SysFont("Verdana", 64)
    if user_board[position[1] - 1][position[0] - 1] == event.key - 48:
        user_board[position[1] - 1][position[0] - 1] = 0
    if helperfunc(event.key - 48, position[1] - 1, position[0] - 1, user_board):
        num = font.render(str(event.key - 48), True, (36, 161, 156))
    else:
        num = font.render(str(event.key - 48), True, (251, 116, 62))
    clear_square(window=window, position=(Y, X))
    window.blit(num, (position[0] * 80 + 24, position[1] * 80 + 12))
    # pygame.display.update()


def clear_square(window, position):
    x, y = position[1], position[0]
    pygame.draw.rect(window, BACKGROUND_COL, (y * 80 + 10, x * 80 + 5, 60, 70))


def update_board(window, font, user_board, board, solver=False, always_unsolved=False):
    window.fill(BACKGROUND_COL)
    for i in range(10):  # Can be written in one loop if using a single colour
        if i % 3 != 0:  # Remove unnecessary lines
            pygame.draw.line(window, THIN_LINES_COL, (80 + (80 * i), 80), (80 + (80 * i), 800), 2)
            pygame.draw.line(window, THIN_LINES_COL, (80, 80 + (80 * i)), (800, 80 + (80 * i)), 2)
    for i in range(
            10):  # Extra loop written to avoid thin lines being drawn over thick lines (visually less attractive)
        if i % 3 == 0:
            pygame.draw.line(window, THICC_LINES_COL, (80 + (80 * i), 80), (80 + (80 * i), 801),
                             4)  # 801 to smoothen corner
            pygame.draw.line(window, THICC_LINES_COL, (80, 80 + (80 * i)), (801, 80 + (80 * i)), 4)
    for y in range(0, len(user_board[0])):
        for x in range(0, len(user_board[0])):
            if solver == True:
                if user_board[y][x] != always_unsolved[y][x]:
                    num = font.render(str(user_board[y][x]), True, (36, 161, 156))
                    clear_square(window=window, position=(x + 1, y + 1))
                    window.blit(num, ((x + 1) * 80 + 24, (y + 1) * 80 + 12))
                elif user_board[y][x] != 0:
                    num = font.render(str(user_board[y][x]), True, NUMBERS_COL)
                    window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
            else:
                if user_board[y][x] != board[y][x]:
                    old_val = user_board[y][x]
                    user_board[y][x] = 0
                    if helperfunc(old_val, y, x, user_board):
                        num = font.render(str(old_val), True, (36, 161, 156))
                    else:
                        num = font.render(str(old_val), True, (251, 116, 62))
                    user_board[y][x] = old_val
                    clear_square(window=window, position=(x + 1, y + 1))
                    window.blit(num, ((x + 1) * 80 + 24, (y + 1) * 80 + 12))
                elif user_board[y][x] != 0:
                    num = font.render(str(user_board[y][x]), True, NUMBERS_COL)
                    window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
    insturctions(window)


def highlight_square(window, position):
    x, y = position[1], position[0]
    for i in range(2):
        pygame.draw.line(window, (193, 222, 174), ((i * 80) + x * 80, y * 80), ((i * 80) + x * 80, y * 80 + 80), 8)
        pygame.draw.line(window, (193, 222, 174), (x * 80 - 3, (i * 80) + y * 80), (x * 80 + 84, (i * 80) + y * 80), 8)


def insturctions(window):
    font = pygame.font.Font(None, 40)
    press_space = font.render('Press Space to Auto Solve', True, NUMBERS_COL)
    press_n = font.render('Press N for new board', True, NUMBERS_COL)
    window.blit(press_space, (260, 810))
    window.blit(press_n, (260, 840))

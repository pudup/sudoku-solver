import pygame
from colours_and_fonts import *
from animation_funcs import insturctions


# Grid Settings
def draw_grid(window):
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
    pygame.display.update()


# Grid populate
def grid_init(window, font, board):
    for y in range(0, len(board[0])):
        for x in range(0, len(board[0])):
            if board[y][x] != 0:
                num = font.render(str(board[y][x]), True, NUMBERS_COL)
                window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
    insturctions(window)
    pygame.display.update()

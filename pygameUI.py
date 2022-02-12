# Full rewrite
import pygame
import requests
from solverUIHelp import sudoku_solver, helperfunc
from copy import deepcopy

# Colours (from colorhunt.co :>)
BACKGROUND_COL = (251, 229, 229)
THIN_LINES_COL = (255,161,201)
THICC_LINES_COL = (249,72,146)
NUMBERS_COL = (230, 9, 101)

# Global Co-Ords
X = 0
Y = 0

#Get boards from sugoku api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
board = response.json()["board"]
user_board = deepcopy(board)

## Functions
# Input numbers
def add_a_num(window, position, event):
    font = pygame.font.SysFont("Verdana", 64)
    if user_board[position[1]- 1][position[0] - 1] == event.key - 48:
        user_board[position[1]- 1][position[0] - 1] = 0
    if helperfunc(event.key - 48, position[1] - 1, position[0] - 1, user_board):
        num = font.render(str(event.key - 48), True, (36, 161, 156))
    else:
        num = font.render(str(event.key - 48), True, (251, 116, 62))
    clear_square(window=window, position=(Y, X))
    window.blit(num, (position[0] * 80 + 24, position[1] * 80 + 12))
    pygame.display.update()

def clear_square(window, position):
    x, y = position[1], position[0]
    pygame.draw.rect(window, BACKGROUND_COL, (y * 80 + 10, x * 80 + 5, 60, 70))

def update_board(window, font):
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
    pygame.display.update()


#Grid Settings
def draw_grid(window):
    for i in range(10): # Can be written in one loop if using a single colour
        if i % 3 != 0: # Remove unnecessary lines
            pygame.draw.line(window, THIN_LINES_COL, (80 + (80 * i), 80), (80 + (80 * i), 800), 2)
            pygame.draw.line(window, THIN_LINES_COL, (80, 80 + (80 * i)), (800, 80 + (80 * i)), 2)
    for i in range(10): # Extra loop written to avoid thin lines being drawn over thick lines (visually less attractive)
        if i % 3 == 0:
            pygame.draw.line(window, THICC_LINES_COL, (80 + (80 * i), 80), (80 + (80 * i), 801), 4)# 801 to smoothen corner
            pygame.draw.line(window, THICC_LINES_COL, (80, 80 + (80 * i)), (801, 80 + (80 * i)), 4)
    pygame.display.update()

def highlight_square(window, position):
    x, y = position[1], position[0]
    for i in range(2):
        pygame.draw.line(window, (193, 222, 174), ((i * 80) + x * 80, y * 80), ((i * 80) + x * 80, y * 80 + 80), 8)
        pygame.draw.line(window, (193, 222, 174), (x * 80, (i * 80) + y * 80), (x * 80 + 80, (i * 80) + y * 80), 8)
        pygame.display.update()

#Grid populate
def grid_init(window, font):
    for y in range(0, len(board[0])):
        for x in range(0, len(board[0])):
            if board[y][x] != 0:
                num = font.render(str(board[y][x]), True, NUMBERS_COL)
                window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
    pygame.display.update()

#Clear screen
def clr_scr(window):
    window.fill(BACKGROUND_COL)
    pygame.display.update()

# Main loop
def main():
    global X
    global Y
    pygame.init()

    #Window Settings
    window = pygame.display.set_mode((885,900))
    pygame.display.set_caption("Sudoku Solver")
    window.fill(BACKGROUND_COL)
    font = pygame.font.SysFont("Verdana", 64)

    draw_grid(window=window)
    grid_init(window=window, font=font)


    # Board loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # AUTO SOLVER
                    clr_scr(window=window)
                    draw_grid(window=window)
                    sudoku_solver(board)
                    for y in range(0, len(board[0])):
                        for x in range(0, len(board[0])):
                            if board[y][x] != 0:
                                num = font.render(str(board[y][x]), True, NUMBERS_COL)
                                window.blit(num, (((x + 1) * 80) + 24, ((y + 1) * 80) + 12))
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                x, y = position[1] // 80, position[0] // 80
                if ((y * 80) < 80) or ((x * 80) < 80) or ((y * 80) >= 800) or ((x * 80) >= 800):
                    X, Y = 0, 0
                    update_board(window, font)
                else:
                    X, Y = position[1]//80, position[0]//80
                    update_board(window, font)
                    highlight_square(window, (X, Y))
            if event.type == pygame.KEYDOWN:
                if (X, Y) == (0, 0):
                    pass
                elif board[X-1][Y-1] != 0:
                    pass
                elif event.key == 48:
                    clear_square(window=window, position=(Y, X))
                    user_board[X-1][Y-1] = 0
                    pygame.display.update()
                elif 0 < (event.key - 48) < 10: # ASCII Value ';..;'
                    add_a_num(window, (y, x), event)
                    user_board[X-1][Y-1] = event.key - 48







if __name__ == "__main__":
    main()
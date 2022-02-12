# Full rewrite
import pygame
import requests
from solverUIHelp import sudoku_solver

# Colours (from colorhunt.co :>)
BACKGROUND_COL = (251, 229, 229)
THIN_LINES_COL = (255,161,201)
THICC_LINES_COL = (249,72,146)
NUMBERS_COL = (230, 9, 101)

#Get boards from sugoku api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
board = response.json()["board"]

## Functions
# Input numbers
def input_num(window, position):
    font = pygame.font.SysFont("Verdana", 64)
    num = font.render(str(1), True, NUMBERS_COL)
    window.blit(num, (position[0] * 80 + 24, position[1] * 80 + 12))
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
                if event.key == pygame.K_SPACE:
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
                input_num(window, (position[0]//80, position[1]//80))





if __name__ == "__main__":
    main()
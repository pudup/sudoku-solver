# Full rewrite
import pygame
import sys
sys.path.insert(0, "./PyGameComponents")
from PyGameComponents.solverUIHelp import helperfunc
from PyGameComponents.get_new_board import generateBoards
from PyGameComponents.auto_solver import solve_board
from PyGameComponents.colours_and_fonts import *
from PyGameComponents.grid_init import draw_grid, grid_init
from PyGameComponents.animation_funcs import add_a_num, clear_square, update_board, highlight_square
from copy import deepcopy

# Main loop
def main():
    X = 0 # Initial Co-ordinates
    Y = 0
    board, user_board, always_unsolved = generateBoards() # Initial boards
    pygame.init()

    #Window Settings
    window = pygame.display.set_mode((885,900))
    pygame.display.set_caption("Sudoku Solver")
    window.fill(BACKGROUND_COL)
    font = pygame.font.SysFont("Verdana", 64)

    draw_grid(window=window,)
    grid_init(window=window, font=font, board=board)


    # Board loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # AUTO SOLVER
                    solve_board(window, board, always_unsolved,)
                    user_board = board
                    update_board(window, font, user_board, board)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                x, y = position[1] // 80, position[0] // 80
                if ((y * 80) < 80) or ((x * 80) < 80) or ((y * 80) >= 800) or ((x * 80) >= 800):
                    X, Y = 0, 0
                    update_board(window, font, user_board, board)
                else:
                    X, Y = position[1]//80, position[0]//80
                    update_board(window, font, user_board, board)
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
                    add_a_num(window, (y, x), event, user_board, Y, X)
                    user_board[X-1][Y-1] = event.key - 48
                if event.key == 110:
                    getting_new = font.render('Getting New Board', True, NUMBERS_COL)
                    window.blit(getting_new, (170, 10))
                    pygame.display.update()
                    board, user_board, always_unsolved = generateBoards()
                    update_board(window, font, user_board, board)








if __name__ == "__main__":
    main()
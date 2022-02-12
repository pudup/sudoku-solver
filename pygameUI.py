# Full rewrite
import pygame

def main():
    pygame.init()

    #Window Settings
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Sudoku Solver")
    window.fill((255,255,255))

    #Grid Settings


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
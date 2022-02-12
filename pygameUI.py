# Full rewrite
import pygame

def main():
    pygame.init()

    #Window Settings
    window = pygame.display.set_mode((885,900))
    pygame.display.set_caption("Sudoku Solver")
    window.fill((251, 229, 229))

    #Grid Settings
    for i in range(10): # Can be written in one loop if using a single colour
        pygame.draw.line(window, (255,161,201), (80 + (80 * i), 80), (80 + (80 * i), 800), 2)
        pygame.draw.line(window, (255,161,201), (80, 80 + (80 * i)), (800, 80 + (80 * i)), 2)
    for i in range(10): # Extra loop written to avoid thin lines being drawn over thick lines (visually less attractive)
        if i % 3 == 0:
            pygame.draw.line(window, (249, 72, 146), (80 + (80 * i), 80), (80 + (80 * i), 801), 4)
            pygame.draw.line(window, (249, 72, 146), (80, 80 + (80 * i)), (801, 80 + (80 * i)), 4)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
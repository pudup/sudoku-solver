import pygame, sys

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800,800))

# Window Title
pygame.display.set_caption("Didi Game Game")

# Window Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Grid image
grid_image = pygame.image.load('backgr6.png')


# Window loop
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill((200, 200, 200))

    screen.blit(grid_image, (100, 100))
    pygame.display.update()
import pygame, sys

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800,800))

# Window loop
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

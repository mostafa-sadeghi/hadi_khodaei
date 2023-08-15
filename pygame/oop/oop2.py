import pygame

pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600

FPS = 60
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

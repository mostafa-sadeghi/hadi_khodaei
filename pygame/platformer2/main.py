import pygame
from pygame.locals import *
from constants import *
from world import draw_grid, World
from levels.level0_data import world_data
from player import Player


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.init()
sun_img = pygame.image.load("img\sun.png")
sky_img = pygame.image.load("img\sky.png")


player = Player(100, WINDOW_HEIGHT-130)


word = World(world_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_img, (0, 0))
    screen.blit(sun_img, (100, 100))
 
    word.draw(screen)
    draw_grid(screen)
    player.update(screen)

    pygame.display.update()
    clock.tick(FPS)

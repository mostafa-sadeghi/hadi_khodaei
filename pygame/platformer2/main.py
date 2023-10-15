import pygame
from pygame.locals import *
from button import Button
from constants import *
from world import draw_grid, World
from levels.level0_data import world_data
from player import Player


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen2 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.init()
sun_img = pygame.image.load("img\sun.png")
sky_img = pygame.image.load("img\sky.png")
restart_img = pygame.image.load("img/restart_btn.png")


blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
player = Player(100, WINDOW_HEIGHT-130, blob_group, lava_group)
restart_button = Button(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, restart_img)


word = World(world_data, blob_group, lava_group)
game_over = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    word.draw(screen)
    draw_grid(screen)
    game_over = player.update(screen, word.tile_list, game_over)
    blob_group.update()
    blob_group.draw(screen)
    lava_group.draw(screen)

    if game_over == -1:
        restart_button.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

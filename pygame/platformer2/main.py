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
main_menu = True
pygame.init()
sun_img = pygame.image.load("img\sun.png")
sky_img = pygame.image.load("img\sky.png")
restart_img = pygame.image.load("img/restart_btn.png")
start_img = pygame.image.load("img/start_btn.png")
start_img = pygame.transform.scale(start_img, (120, 42))
exit_img = pygame.image.load("img/exit_btn.png")
exit_img = pygame.transform.scale(exit_img, (120, 42))

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()


player = Player(100, WINDOW_HEIGHT-130, blob_group, lava_group, exit_group)
restart_button = Button(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, restart_img)
start_button = Button(WINDOW_WIDTH/2 - 200, WINDOW_HEIGHT/2, start_img)
exit_button = Button(WINDOW_WIDTH/2 + 70, WINDOW_HEIGHT/2, exit_img)


word = World(world_data, blob_group, lava_group, exit_group)
game_over = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(sky_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    if main_menu:
        if exit_button.draw(screen):
            running = False
        if start_button.draw(screen):
            main_menu = False
    else:
        word.draw(screen)
        draw_grid(screen)
        game_over = player.update(screen, word.tile_list, game_over)
        blob_group.update()
        blob_group.draw(screen)
        lava_group.draw(screen)
        exit_group.draw(screen)

        if game_over == -1:
            if restart_button.draw(screen):
                game_over = 0
                player.reset(100, WINDOW_HEIGHT-130,
                             blob_group, lava_group, exit_group)

    pygame.display.update()
    clock.tick(FPS)

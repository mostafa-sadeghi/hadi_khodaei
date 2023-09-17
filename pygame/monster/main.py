import random

from pygame.sprite import Sprite
import pygame
from game import Game
from space.player import Player
from config import WIN_WIDTH, WIN_HEIGHT

pygame.init()

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()


my_player_group = pygame.sprite.Group()
player = Player()
my_player_group.add(player)

monster_group = pygame.sprite.Group()

game = Game(player, monster_group)
game.start_new_round()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.warp()

    display_surface.fill((0, 0, 0))
    my_player_group.update()
    my_player_group.draw(display_surface)
    my_player_group.update()
    my_player_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)
    game.update()
    game.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

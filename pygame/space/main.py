import pygame
from config import *
from player import Player
from game import Game
pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

player = Player(player_bullet_group)
alien_group = pygame.sprite.Group()

game = Game(player, alien_group, player_bullet_group, alien_bullet_group)
game.start_new_round()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    display_surface.fill((0, 0, 0))
    player_bullet_group.update()
    player_bullet_group.draw(display_surface)
    alien_bullet_group.update()
    alien_bullet_group.draw(display_surface)
    alien_group.update()
    alien_group.draw(display_surface)
    player.update()
    player.draw(display_surface)
    game.draw(display_surface)
    game.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame
from constants import *
from soldier import Soldier, Enemy
from world import World
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

player = Soldier('player',200,200, 3, 5,player_bullet_group)
enemy = Enemy('enemy',500,200, 3, 5,enemy_bullet_group)
world = World()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_LSHIFT:
                player.shooting = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LSHIFT:
                player.shooting = False
    if player.alive:
        if player.shooting:
            print("player shooting")
            player.shoot()
        if player.in_air:
            player.update_action(2)
        elif player.moving_left or player.moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
    
    world.draw_bg(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    player.move()
    player.update_animation()
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.update()
    clock.tick(FPS)


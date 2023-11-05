import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, health, animation_list, x, y, speed):
        super().__init__()
        self.health = health
        self.animation_list = animation_list
        self.speed = speed
        self.alive = True

        self.action = 0
        self.frame_index = 0

        self.attack_cooldown = 1000
        self.last_attack = pygame.time.get_ticks()

        self.update_time = pygame.time.get_ticks()

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, target, bullet_group):
        if self.alive:
            if self.rect.right > target.rect.left:
                self.action = 1

            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25

            if self.health <= 0:
                target.money += 100
                target.score += 100
                self.action = 2
                self.alive = False

            if self.action == 0:
                self.rect.x += self.speed

            if self.action == 1:
                if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
                    target.health -= 25
                    self.last_attack = pygame.time.get_ticks()
                    if target.health < 0:
                        target.health = 0

               

        self.update_animation()

    def update_animation(self):
        ANIMATION_COOLDOWN = 50
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:

            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.frame_index = 0

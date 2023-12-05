import pygame
from pygame.sprite import Sprite
from constants import *
class Bullet(Sprite):
    def __init__(self,x,y, direction,source,target) -> None:
        super().__init__()

        self.speed = 10
        self.image = pygame.image.load("img/icons/bullet.png")
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        self.source = source
        self.target = target


    def update(self):
        self.rect.x += self.direction * self.speed

        if self.rect.right > SCREEN_WIDTH or self.rect.left <0:
            self.kill()

        # if pygame.sprite.spritecollide(self.player, self.player.bullet_group, True):
        #     if self.player.alive:
        #         self.player.health -= 5
        if pygame.sprite.spritecollide(self.target, self.source.bullet_group, True):
            
            if self.target.alive:
                print(self.target.health)
                self.target.health -= 15
                print(self.target.health)


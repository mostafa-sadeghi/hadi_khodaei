import pygame
from pygame.sprite import Sprite
from constants import *
class Bullet(Sprite):
    def __init__(self,x,y, direction) -> None:
        super().__init__()

        self.speed = 10
        self.image = pygame.image.load("img/icons/bullet.png")
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction 


    def update(self):
        self.rect.x += self.direction * self.speed

        if self.rect.right > SCREEN_WIDTH or self.rect.left <0:
            self.kill()

        # TODO check collision with player and enemy
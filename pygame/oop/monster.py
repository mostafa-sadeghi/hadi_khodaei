import random
from pygame.sprite import Sprite
import pygame
class Monster(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("pygame\\oop\\monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = random.randint(1,10)
        


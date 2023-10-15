from pygame.sprite import Sprite
import pygame
from constants import *


class Lava(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        img = pygame.image.load("img\lava.png")
        self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

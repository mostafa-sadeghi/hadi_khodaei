from pygame.sprite import Sprite
import pygame
from constants import *
from get_abs_path import resource_path

class Door(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(resource_path("img\exit.png")), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

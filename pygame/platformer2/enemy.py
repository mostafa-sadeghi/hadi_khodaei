from pygame.sprite import Sprite
import pygame


class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 50:
            self.move_counter *= -1
            self.move_direction *= -1

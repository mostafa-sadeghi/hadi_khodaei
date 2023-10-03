import pygame
from pygame.locals import *
from constants import *


class Player:
    def __init__(self, x, y):

        self.images_right = []
        self.images_left = []
        self.index = 0
        for i in range(1, 5):
            img = pygame.image.load(f'img\guy{i}.png')
            img_right = pygame.transform.scale(img, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vel_y = 0
        self.jumped = False

    def update(self, screen):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and not self.jumped:
            self.vel_y -= 15
            self.jumped = True
        if not keys[K_SPACE]:
            self.jumped = False
        if keys[K_LEFT]:
            dx -= 5

        if keys[K_RIGHT]:
            dx += 5

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10

        dy += self.vel_y
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            dy = 0

        screen.blit(self.image, self.rect)

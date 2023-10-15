import pygame
from pygame.locals import *
from constants import *


class Player:
    def __init__(self, x, y, blob_group, lava_group):

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.blob_group = blob_group
        self.lava_group = lava_group
        for i in range(1, 5):
            img = pygame.image.load(f'img\guy{i}.png')
            img_right = pygame.transform.scale(img, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.dead_image = pygame.image.load("img/ghost.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.counter = 0

    def update(self, screen, tile_list, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        if game_over == 0:
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and not self.jumped:
                self.vel_y -= 15
                self.jumped = True
            if not keys[K_SPACE]:
                self.jumped = False
            if keys[K_LEFT]:
                dx -= 5
                self.direction = -1
                self.counter += 1

            if keys[K_RIGHT]:
                dx += 5
                self.direction = 1
                self.counter += 1

            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0

                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10

            dy += self.vel_y

            for tile in tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom

            if pygame.sprite.spritecollide(self, self.lava_group, False):

                game_over = -1

            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                dy = 0
        elif game_over == -1:

            self.image = self.dead_image
            if self.rect.y > 150:
                self.rect.y -= 5

        screen.blit(self.image, self.rect)
        return game_over

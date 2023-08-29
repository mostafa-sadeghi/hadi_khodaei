import random
import pygame
from pygame.sprite import Sprite
from config import WIN_WIDTH, WIN_HEIGHT


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

        self.type = monster_type  # 0=>blue,     1=> green,       2=> purple,     3 => yellow
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity
        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.dx *= -1
        if self.rect.top <= 100 or self.rect.bottom >= WIN_HEIGHT - 100:
            self.dy *= -1

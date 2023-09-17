import random
import pygame

from alienBullet import AlienBullet


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("assets/alien_fire.wav")

    def update(self):
        """Update the alien"""
        self.rect.x += self.direction*self.velocity

        if random.randint(0, 1000) > 999:
            self.fire()

    def fire(self):
        pass

    def reset(self):
        """Reset the alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1

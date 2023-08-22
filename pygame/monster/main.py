import random
from typing import Any
from pygame.sprite import Sprite
import pygame

pygame.init()
WIN_WIDTH = 1200
WIN_HEIGHT = 700
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()


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
        if self.rect.top <= 100 or self.rect.bottom >= WIN_WIDTH - 100:
            self.dy *= -1


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIN_HEIGHT
        self.rect.bottom = WIN_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")
        self.warp_sound = pygame.mixer.Sound("assets/warp.wav")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity

        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.velocity

        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity

        if keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT - 100:
            self.rect.y += self.velocity

    def warp(self):
        pass
        # TODO

    def reset(self):
        pass
        # TODO


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.round_time = 0

        self.player = player
        self.monster_group = monster_group
        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.target_monster_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]
        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WIN_WIDTH/2
        self.target_monster_rect.top = 30

    def update(self):
        self.check_collisions()

    def draw(self):
        # Define Some Colors with list
        # Render these texts:
        # Score text
        # Lives text
        # round text
        # time text
        # warps_text

        # and blit theme into the display surface

        # TODO draw rect around monster target
        # pygame.draw.rect(display_surface, )
        # draw rect around arena (game world)


my_player_group = pygame.sprite.Group()
player = Player()
my_player_group.add(player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player_group.update()
    my_player_group.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

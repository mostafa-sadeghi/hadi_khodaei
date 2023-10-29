import pygame
from pygame.sprite import Sprite
import math

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("assets/bg.png")
castle_100 = pygame.image.load("assets/castle/castle_100.png")
bullet_img = pygame.image.load("assets/bullet.png")
# TODO change bullet size if is not good
bullet_img = pygame.transform.scale(bullet_img, (10, 10))
bullet_group = pygame.sprite.Group()

enemy_animations = []
enemy_types = ['knight']
enemy_health = [75]

animation_types = ['walk', 'attack', 'death']

for enemy in enemy_types:
    animation_list = []
    for animation in animation_types:
        temp_list = []
        for i in range(20):
            img = pygame.image.load(
                f'assets/enemies/{enemy}/{animation}/{i}.png')
            img = pygame.transform.scale(img, (64, 64))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)

print(enemy_animations)


class Castle:
    def __init__(self, image100, x, y, scale) -> None:
        self.health = 1000
        self.fired = False
        self.max_health = self.health
        self.image100 = pygame.transform.scale(
            image100, (image100.get_width()*scale, image100.get_height()*scale))
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.image = self.image100
        screen.blit(self.image, self.rect)

    def shoot(self):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.midleft[0]
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        # pygame.draw.line(screen, (255, 255, 255), self.rect.midleft, pos)
        if pygame.mouse.get_pressed()[0] and not self.fired:
            self.fired = True
            bullet = Bullet(
                bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)

            bullet_group.add(bullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False


class Bullet(Sprite):
    def __init__(self, image, x, y, angle):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.speed = 10
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle)) * self.speed

    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH or self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.kill()
        self.rect.x += self.dx
        self.rect.y += self.dy


castle = Castle(castle_100, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    castle.shoot()
    castle.draw()
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

import random
import pygame
from pygame.sprite import Sprite
import math
from button import Button

from enemy import Enemy

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('FiraCode', 32)
font60 = pygame.font.SysFont('FiraCode', 60)


clock = pygame.time.Clock()
FPS = 60

level = 1
level_difficulty = 0
target_difficulty = 1000
DIFFICULTY_MULTIPLIER = 1.1
game_over = False
next_level = False


enemies_alive = 0
last_enemy = pygame.time.get_ticks()


bg = pygame.image.load("assets/bg.png")
castle_100 = pygame.image.load("assets/castle/castle_100.png")
castle_50 = pygame.image.load("assets/castle/castle_50.png")
castle_25 = pygame.image.load("assets/castle/castle_25.png")
bullet_img = pygame.image.load("assets/bullet.png")

repair_img = pygame.image.load("assets/repair.png")
armour_img = pygame.image.load("assets/armour.png")


# TODO change bullet size if is not good
bullet_img = pygame.transform.scale(bullet_img, (10, 10))
bullet_group = pygame.sprite.Group()

enemy_animations = []
enemy_types = ['knight', 'goblin', 'purple_goblin', 'red_goblin']
enemy_health = [75, 100, 125, 150]

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

enemy_group = pygame.sprite.Group()


class Castle:
    def __init__(self, image100, image50, image25, x, y, scale) -> None:
        self.health = 1000
        self.fired = False
        self.max_health = self.health
        self.image100 = pygame.transform.scale(
            image100, (image100.get_width()*scale, image100.get_height()*scale))
        self.image50 = pygame.transform.scale(
            image50, (image50.get_width()*scale, image50.get_height()*scale))
        self.image25 = pygame.transform.scale(
            image25, (image25.get_width()*scale, image25.get_height()*scale))
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.money = 1000
        self.score = 0

    def draw(self):
        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100

        screen.blit(self.image, self.rect)

    def shoot(self, action):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.midleft[0]
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.atan2(y_dist, x_dist)
        # pygame.draw.line(screen, (255, 255, 255), self.rect.midleft, pos)
        if pygame.mouse.get_pressed()[0] and not self.fired and (not action['repair_button'] or not action['armour_button']):
            self.fired = True
            bullet = Bullet(
                bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)

            bullet_group.add(bullet)
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False


    def repair(self):
        if self.money >= 1000 and self.health < self.max_health:
            self.health += 500
            self.money -= 1000
            if castle.health > castle.max_health:
                castle.health = castle.max_health

    def armour(self):
        if self.money >= 500:
            self.max_health += 250
            self.money -= 500



class Tower(Sprite):
    def __init__(self, image100, image50, image25, x, y, scale):
        self.image100 = pygame.transform.scale(
            image100, (image100.get_width()*scale, image100.get_height()*scale))
        self.image50 = pygame.transform.scale(
            image50, (image50.get_width()*scale, image50.get_height()*scale))
        self.image25 = pygame.transform.scale(
            image25, (image25.get_width()*scale, image25.get_height()*scale))
        self.image = self.image100
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, enemy_group):
        pass





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


castle = Castle(castle_100, castle_50, castle_25,
                SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)

repair_button = Button(SCREEN_WIDTH - 220, 10, pygame.transform.scale(repair_img, (30,30)))
armour_button = Button(SCREEN_WIDTH - 80, 10, pygame.transform.scale(armour_img, (30,30)))



def draw_text(text, font, color, x,y):
    text = font.render(text, True, color)
    screen.blit(text, (x,y))


def show_info():
    draw_text(f'Money:{castle.money}', font, (255,255,255), 10,10)
    draw_text(f'Score:{castle.money}', font, (10,10,40), 10,40)
    draw_text(f'Score:{level}', font, (10,10,40), SCREEN_WIDTH/2,10)
    draw_text(f'Health:{castle.health}', font, (10,10,40), SCREEN_WIDTH-230,SCREEN_HEIGHT-50)




class Crosshair:
    def __init__(self, scale):
        image = pygame.image.load('assets/crosshair.png')
        self.image = pygame.transform.scale(
            image, (scale * image.get_width(), scale * image.get_height()))
        self.rect = self.image.get_rect()

        pygame.mouse.set_visible(False)

    def draw(self):
        self.rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)


crosshair = Crosshair(0.03)

running = True
action = {
'repair_button':True,
'armour_button':True,
}
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if repair_button.draw(screen):
        action['repair_button'] = True
        
        castle.repair()
    else:
        action['repair_button'] = False
    
    
    if armour_button.draw(screen):
        action['armour_button'] = True
        action['repair_button'] = True
        print("inside")
        castle.armour()


    if level_difficulty < target_difficulty:
        if pygame.time.get_ticks() - last_enemy > 1000:
            last_enemy = pygame.time.get_ticks()
            e = random.randint(0, len(enemy_types)-1)

            enemy = Enemy(enemy_health[e], enemy_animations[e], 200, 500, 1)
            enemy_group.add(enemy)
            level_difficulty += enemy_health[e]

    if level_difficulty >= target_difficulty:
        enemies_alive = 0
        for enemy in enemy_group:
            if enemy.alive:
                enemies_alive += 1

        if enemies_alive == 0 and not next_level:
            level_reset_time = pygame.time.get_ticks()
            next_level = True
    if next_level == True:
        draw_text('LEVEL COMPLETE...', font60, (255,255,255),200,300)
        if pygame.time.get_ticks() - level_reset_time > 1500:
            next_level = False        
            level_difficulty = 0
            target_difficulty *= DIFFICULTY_MULTIPLIER
            enemy_group.empty()
            level += 1


    show_info()
    
    castle.shoot(action)
    castle.draw()
    bullet_group.update()
    bullet_group.draw(screen)
    enemy_group.update(castle, bullet_group)
    enemy_group.draw(screen)
    crosshair.draw()
    pygame.display.update()
    clock.tick(FPS)

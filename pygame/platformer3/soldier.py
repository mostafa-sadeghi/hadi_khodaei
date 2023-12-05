import os
from pygame.sprite import Sprite
import pygame

from bullet import Bullet


class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale,speed,ammo, bullet_group):
        super().__init__()
        self.alive = True
        self.bullet_group = bullet_group
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.flip = False
        self.in_air = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.vel_y = 0
        self.ammo = ammo
        self.start_ammo = ammo
        self.health = 100
        self.max_health = self.health
        self.shooting = False
        self.shoot_cooldown = 20
        self.update_time = pygame.time.get_ticks()
        animation_types = ['Idle', 'Run','Jump','Death']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
                img = pygame.transform.scale(img, (img.get_width()* scale, img.get_height() * scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)


        self.image= self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center=(x,y))

    def move(self):
        dx = 0
        dy = 0
        if self.moving_left:
            dx -= self.speed
            self.direction = -1
            self.flip = True
        if self.moving_right:
            dx += self.speed
            self.direction = 1
            self.flip = False

        if self.jump and not self.in_air:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        self.vel_y += 1
        dy += self.vel_y

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy
    
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image= self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.frame_index = 0
        
        self.check_alive()


    def update_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    
    def shoot(self, enemy):
        if self.shoot_cooldown >0:
            self.shoot_cooldown -= 1
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + self.image.get_width(), self.rect.centery, self.direction, self, enemy)
            self.bullet_group.add(bullet)
            self.ammo -= 1

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0 
            self.alive = False
            self.update_action(3)



    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

  
class Enemy(Soldier):
    def __init__(self, char_type, x, y, scale, speed,ammo, bullet_group):
        super().__init__(char_type, x, y, scale, speed,ammo,bullet_group)
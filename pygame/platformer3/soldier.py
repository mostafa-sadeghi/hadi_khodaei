import os
from pygame.sprite import Sprite
import pygame


class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale,speed):
        super().__init__()
        self.alive = True
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
            self.frame_index = 0


    def update_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    
    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

  
class Enemy(Soldier):
    def __init__(self, char_type, x, y, scale, speed):
        super().__init__(char_type, x, y, scale, speed)
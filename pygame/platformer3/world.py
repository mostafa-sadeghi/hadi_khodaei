import pygame
from constants import *

class World:
    def draw_bg(self,screen):
        screen.fill((144,201,120))
        pygame.draw.line(screen, (255,10,237), (0,300),(SCREEN_WIDTH, 300))
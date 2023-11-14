import pygame
class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.startx = x
        self.starty = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, screen):

        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                # self.rect.x = pos[0]-self.image.get_width()/2
                # self.rect.y = pos[1] - self.image.get_height()/2
                action = True
            # if not pygame.mouse.get_pressed()[0]:
            #     self.rect.x = self.startx
            #     self.rect.y = self.starty


        screen.blit(self.image, self.rect)
        return action
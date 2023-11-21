import pygame
class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.startx = x
        self.starty = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen):

        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                # self.rect.x = pos[0]-self.image.get_width()/2
                # self.rect.y = pos[1] - self.image.get_height()/2
                action = True
                self.clicked = True
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
            #     self.rect.x = self.startx
            #     self.rect.y = self.starty


        screen.blit(self.image, self.rect)
        return action
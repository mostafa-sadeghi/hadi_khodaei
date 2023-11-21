import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image_int, main_group, sub_group=""):
        super().__init__()
        if image_int == 1:
            self.image = pygame.image.load("assets/dirt.png")
        elif image_int == 2:
            self.image = pygame.image.load("assets/grass.png")
            sub_group.add(self)
        else:
            self.image = pygame.image.load("assets/water.png")
            sub_group.add(self)

        main_group.add(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self, display_surface):
        pygame.draw.rect(display_surface, (0,0,255), self.rect, 1)




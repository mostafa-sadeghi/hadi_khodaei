import pygame
from constants import *
from door import Door
from enemy import Enemy
from lava import Lava
from get_abs_path import resource_path

def draw_grid(screen):
    for line in range(12):
        pygame.draw.line(screen, (255, 255, 255),
                         (0, line*TILE_SIZE), (WINDOW_WIDTH, line*TILE_SIZE))
        pygame.draw.line(screen, (255, 255, 255),
                         (line*TILE_SIZE, 0), (line*TILE_SIZE, WINDOW_HEIGHT))


class World:
    def __init__(self, data, blob_group, lava_group, exit_group) -> None:
        self.tile_list = []
        self.blob_group = blob_group
        self.lava_group = lava_group
        self.exit_button = exit_group
        dirt_img = pygame.image.load(resource_path("img\dirt.png"))
        grass_img = pygame.image.load(resource_path("img\grass.png"))
        for row_index, row in enumerate(data):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    img = pygame.transform.scale(
                        dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                        grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    blob = Enemy(col_index * TILE_SIZE,
                                 row_index * TILE_SIZE + 16)
                    self.blob_group.add(blob)
                if tile == 6:
                    lava = Lava(col_index * TILE_SIZE,
                                row_index * TILE_SIZE)
                    self.lava_group.add(lava)
                if tile == 8:
                    door = Door(col_index * TILE_SIZE,
                                row_index * TILE_SIZE)
                    self.exit_button.add(door)

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

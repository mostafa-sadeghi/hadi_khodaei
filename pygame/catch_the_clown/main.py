from random import choice
import pygame

pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600

FPS = 60
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")
display_surface.set_alpha(128)
bg_image = pygame.image.load("background.png")
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)


red = pygame.Color(255, 255, 255)

font = pygame.font.SysFont("Terminal", 64)
my_text = font.render("Hello", True, red)
my_text_rect = my_text.get_rect()
my_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

clown_image = pygame.transform.scale(pygame.image.load("clown.png"), (64, 64))
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

dx = choice([-1, 1])
dy = choice([-1, 1])
clown_velocity = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_rect.collidepoint(event.pos):
                print('catched!!!')

    clown_rect.x += dx * clown_velocity
    clown_rect.y += dy * clown_velocity

    if clown_rect.right > WINDOW_WIDTH or clown_rect.left < 0:
        dx *= -1
    if clown_rect.bottom > WINDOW_HEIGHT or clown_rect.top < 0:
        dy *= -1

    display_surface.blit(bg_image, bg_rect)
    display_surface.blit(clown_image, clown_rect)
    display_surface.blit(my_text, my_text_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

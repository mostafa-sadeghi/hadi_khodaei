from random import randint
import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GREEN = (0, 255, 0)
DarkGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
FOOD_STARTING_VELOCITY = 10
FOOD_ACCELERATION = 0.5

FPS = 60
clock = pygame.time.Clock()

score = 0
player_lives = PLAYER_STARTING_LIVES
food_velocity = FOOD_STARTING_VELOCITY


display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")
dragon_left_image = pygame.image.load("assets/images/dragon_left.png")
dragon_left_image_rect = dragon_left_image.get_rect()
dragon_left_image_rect.topleft = (0, 0)
dragon_right_image = pygame.transform.flip(
    pygame.image.load("assets/images/dragon_left.png"),
    True, False)
dragon_right_image_rect = dragon_right_image.get_rect()
dragon_right_image_rect.topright = (WINDOW_WIDTH, 0)


player_image = pygame.transform.scale(dragon_right_image, (96, 96))
player_rect = player_image.get_rect()
player_rect.midleft = (32, WINDOW_HEIGHT/2)

food_image = pygame.image.load("assets/images/food.png")
food_rect = food_image.get_rect()

food_rect.center = (WINDOW_WIDTH + 100, randint(128, WINDOW_HEIGHT - 50))


# font = pygame.font.SysFont("arial", 32)
font = pygame.font.Font("assets/fonts/DragonHunter.otf", 48)

title_text = font.render("Dragon Game", True, GREEN, DarkGREEN)
title_text_rect = title_text.get_rect()
title_text_rect.top = 0
title_text_rect.centerx = WINDOW_WIDTH/2

score_text = font.render(f"Score: {score}", True, GREEN, DarkGREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (128, 50)

lives_text = font.render(f"Lives: {player_lives}", True, GREEN, DarkGREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH-128, 50)


pygame.mixer.music.load("assets/sounds/ftd_background_music.wav")
pygame.mixer.music.play(-1)


coin_sound = pygame.mixer.Sound("assets/sounds/coin_sound.wav")
miss_sound = pygame.mixer.Sound("assets/sounds/miss_sound.wav")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY
    if keys[pygame.K_UP] and player_rect.top > 128:
        player_rect.y -= PLAYER_VELOCITY

    if food_rect.x < 0:
        food_rect.center = (WINDOW_WIDTH + 100,
                            randint(128, WINDOW_HEIGHT - 50))

    food_rect.x -= food_velocity

    if player_rect.colliderect(food_rect):
        coin_sound.play()
        food_rect.center = (WINDOW_WIDTH + 100,
                            randint(128, WINDOW_HEIGHT - 50))

    display_surface.fill(BLACK)

    display_surface.blit(dragon_left_image,
                         dragon_left_image_rect)
    display_surface.blit(dragon_right_image,
                         dragon_right_image_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    pygame.draw.line(display_surface, WHITE,
                     (0, 128), (WINDOW_WIDTH, 128), 4)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(food_image, food_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

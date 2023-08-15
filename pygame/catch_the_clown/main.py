# from random import choice
# import pygame

# pygame.init()
# WINDOW_WIDTH = 945
# WINDOW_HEIGHT = 600

# FPS = 60
# clock = pygame.time.Clock()

# display_surface = pygame.display.set_mode((WINDOW_WIDTH,
#                                            WINDOW_HEIGHT)).convert_alpha()
# pygame.display.set_caption("Catch the Clown")

# bg_image = pygame.image.load("background.png").convert_alpha()
# bg_rect = bg_image.get_rect()
# bg_rect.topleft = (0, 0)


# red = pygame.Color(255, 255, 255, 120)

# font = pygame.font.SysFont("Terminal", 64)
# my_text = font.render("Hello", True, (255, 0, 0), (255, 255, 255, 120))
# my_text_rect = my_text.get_rect()
# my_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

# clown_image = pygame.transform.scale(pygame.image.load("clown.png"), (64, 64))
# clown_rect = clown_image.get_rect()
# clown_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

# dx = choice([-1, 1])
# dy = choice([-1, 1])
# clown_velocity = 5
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if clown_rect.collidepoint(event.pos):
#                 print('catched!!!')

#     clown_rect.x += dx * clown_velocity
#     clown_rect.y += dy * clown_velocity

#     if clown_rect.right > WINDOW_WIDTH or clown_rect.left < 0:
#         dx *= -1
#     if clown_rect.bottom > WINDOW_HEIGHT or clown_rect.top < 0:
#         dy *= -1

#     display_surface.blit(bg_image, bg_rect)
#     display_surface.blit(clown_image, clown_rect)
#     display_surface.blit(my_text, my_text_rect)

#     pygame.display.update()
#     clock.tick(FPS)
# pygame.quit()


# TODO

# numbers = [1, 2, 7, 9, 3, 4]
# مرتب سازی صعودی
# مرتب سازی نزولی
# sort    sorted    nested for

# راهنمایی
# numbers[0], numbers[1] = numbers[1], numbers[0]

# products = [("productOne", 1000), ("productTwo", 200), ("productThree", 500)]
# مرتب سازی صعودی بر اساس قیمت


# def my_func(row, column):
#     if row >= 7 or column >= 7 or row < 0 or column < 0:
#         return ''

#     if row % 2 == column % 2:
#         return 'white'

#     else:
#         return 'black'


# assert my_func(2, 2) == 'white', "failure"
# assert my_func(2, 1) == 'black', "failure"
# assert my_func(9, 2) == '', "failure"
# assert my_func(0, 0) == 'white', "failure"
# assert my_func(3, 3) == 'white', "failure"
# assert my_func(3, 4) == 'black', "failure"


# message = "The sun"
# old_text = "sun"
# new_text = "moon"

# print(message.replace(old_text, new_text))

# message = "The sun is very nice. i like the sun"
# old_text = "sun"
# new_text = "moon"
# print(message.replace(old_text, new_text))


# def my_replace(text, old_text, new_text):
#     res = ""
#     i = 0
#     while i < len(text):
#         if text[i:i+len(old_text)] == old_text:
#             res += new_text
#             i += len(old_text)
#         else:
#             res += text[i]
#             i+=1

#     return res


# print(my_replace("the sun is nice", "sun", "moon"))


# def get_time(seconds):
#     pass


# """
# 30      =>      30s
# 60      =>      1m
# 61      =>      1m 1s
# 3600    =>      1h
# 3601    =>      1h 1s


# """


"""
تابعی بنویس که لیستی از اعدا را بگیرد و کوچکترین و نیز بزرگترین را برگرداند
تابعی بنویس که لیستی از اعدا را بگیرد و عدد میانه یا وسط را برگرداند
[1,3,2,4,6,7,8,5,9] => 5

تابعی بنویس که لیستی از اعداد را بگیرد و عدد پرتکرار را برگرداند یعنی عددی که بیشتر از همه تکرار شده است


"""


# import random


# def rollDice(num):
#     total = 0
#     for i in range(num):
#         total += random.randint(1, 6)

#     return total

# print(rollDice(1000))
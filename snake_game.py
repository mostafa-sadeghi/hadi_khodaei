from turtle import Screen, Turtle
from time import sleep

def move_snake():
    if snake_head.direction == "up":
        snake_y_position = snake_head.ycor()
        snake_y_position += 20
        snake_head.sety(snake_y_position)


window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)

snake_head = Turtle()
snake_head.shape("square")
snake_head.speed("fastest")
snake_head.penup()
snake_head.direction = "up"



running = True
while running:
    window.update()
    move_snake()
    sleep(0.1)



# def my_func(number):
#    return number % 2 == 0

# print(my_func(4))
# def my_func(number):
#    print(number % 2 == 0)
#    return "balalalalal"

# print(my_func(4))




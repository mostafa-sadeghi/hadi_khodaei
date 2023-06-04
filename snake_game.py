from turtle import Screen, Turtle
from time import sleep
from random import randint


def move_snake():
    if snake_head.direction == "up":
        snake_y_position = snake_head.ycor()
        snake_y_position += 20
        snake_head.sety(snake_y_position)
    if snake_head.direction == "down":
        snake_y_position = snake_head.ycor()
        snake_y_position -= 20
        snake_head.sety(snake_y_position)
    if snake_head.direction == "right":
        snake_x_position = snake_head.xcor()
        snake_x_position += 20
        snake_head.setx(snake_x_position)
    if snake_head.direction == "left":
        snake_x_position = snake_head.xcor()
        snake_x_position -= 20
        snake_head.setx(snake_x_position)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)
snake_head = Turtle()
snake_head.shape("square")
snake_head.speed("fastest")
snake_head.penup()
snake_head.direction = ""

food = Turtle()
food.speed("fastest")
food.shape("circle")
food.shapesize(0.4, 0.4)
food.color("red")
food.penup()
food_x_start_position = randint(-300, 300)
food_y_start_position = randint(-300, 300)
food.goto(food_x_start_position, food_y_start_position)

snake_body = []


window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')


running = True
while running:
    window.update()
    if snake_head.distance(food) < 15:
        food_x_position = randint(-300, 300)
        food_y_position = randint(-300, 300)
        food.goto(food_x_position, food_y_position)
        new_tail = Turtle()
        new_tail.shape("square")
        new_tail.speed("fastest")
        new_tail.penup()
        new_tail.color("grey")
        snake_body.append(new_tail)

    for i in range(len(snake_body) - 1, 0, -1):
        x_pos_of_prev_i = snake_body[i-1].xcor()
        y_pos_of_prev_i = snake_body[i-1].ycor()
        snake_body[i].goto(x_pos_of_prev_i, y_pos_of_prev_i)

    if len(snake_body) > 0:
        snake_last_head_x = snake_head.xcor()
        snake_last_head_y = snake_head.ycor()
        snake_body[0].goto(snake_last_head_x, snake_last_head_y)

    move_snake()
    sleep(0.1)


# def my_func(number):
#    return number % 2 == 0

# print(my_func(4))
# def my_func(number):
#    print(number % 2 == 0)
#    return "balalalalal"

# print(my_func(4))

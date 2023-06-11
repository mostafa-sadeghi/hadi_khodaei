from turtle import Screen
from time import sleep
from snake_game_utils import move_snake, make_turtle, change_turtle_object_position_in_random_place, reset

# TODO بقیه توابع را به ماژول کمکی منتقل


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
snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
food.shapesize(0.4, 0.4)
change_turtle_object_position_in_random_place(food)
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
        change_turtle_object_position_in_random_place(food)
        new_tail = make_turtle("square", "grey")
        snake_body.append(new_tail)

    for i in range(len(snake_body) - 1, 0, -1):
        x_pos_of_prev_i = snake_body[i-1].xcor()
        y_pos_of_prev_i = snake_body[i-1].ycor()
        snake_body[i].goto(x_pos_of_prev_i, y_pos_of_prev_i)

    if len(snake_body) > 0:
        snake_last_head_x = snake_head.xcor()
        snake_last_head_y = snake_head.ycor()
        snake_body[0].goto(snake_last_head_x, snake_last_head_y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset(snake_head, snake_body)

    move_snake(snake_head)

    # TODO چک کردن برخورد با بدن مار
    sleep(0.1)

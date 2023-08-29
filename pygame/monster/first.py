COLORS = ("red", "green", "blue")


def change_color(color):
    if color in COLORS:
        print(f"color changed to {color}")
    else:
        print(f"{color} is not defined!!!")

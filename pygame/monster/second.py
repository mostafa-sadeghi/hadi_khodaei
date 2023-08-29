# import first

# color_user = input("enter your color: ")
# first.change_color(color_user)


from first import COLORS, change_color


color_user = input("enter your color: ")
change_color(color_user)

print("valid colors", COLORS)

# message = "Welcome to python class.\nwelcome to pygame class.\nwelcome to django class."
# print(message)
# message = '''Welcome to python class.
# welcome to pygame class.
# welcome to django class.'''
# print(message)

# import colorama
# colorama.init()

from colorama import init, Fore, Back, Style
init()
# message_1 = "python base class."
# message_2 = "pygame base class."
# message_3 = "data science class"
# message_4 = "web development class"

# print(Fore.RED + Back.CYAN + message_1)
# print(Fore.GREEN + Back.BLACK + message_2)
# print(Fore.LIGHTYELLOW_EX + Back.RED + message_3)
# print(Fore.YELLOW + Back.MAGENTA + message_4)
# message = f'''{Fore.RED + Back.CYAN}Welcome to python class.{Style.RESET_ALL}
# {Fore.GREEN + Back.BLUE}welcome to pygame class.{Style.RESET_ALL}
# {Fore.YELLOW + Back.MAGENTA}welcome to django class.{Style.RESET_ALL}'''
# print(message)
# print(message.split('\n'))

message = '''Welcome to python class.
welcome to pygame class.
welcome to django class.
welcome to ML class.
welcome to Neural Network class.
welcome to JavaScript class.'''
foreground_colors = (Fore.RED, Fore.BLUE, Fore.GREEN)
background_colors = (Back.WHITE, Back.RED, Back.MAGENTA)
lines = []
line = ''
for index, char in enumerate(message):
    line += char
    if char == '\n':
        lines.append(line[:-1])
        line = ''
    if index == len(message)-1:
        lines.append(line)
# print(lines)
for i in range(len(lines)):
    print(foreground_colors[i % 3] + background_colors[i %
          3] + lines[i] + Style.RESET_ALL)


# for index, char in enumerate(message):
#     line += char
#     if char == '\n':
#         lines.append(line[:-1])
#         line = ''
# else:
#     lines.append(line)
# print(lines)


# exercise : هریک از خطوط مسیج بالا به صورت ترتیبی یکی از رنگ های متن و پیس زمینه را از
# foreground_colors
# ,
# background_colors
# بگیرد

# for n in [1, 2, 6, 8, 90]:
#     if n == 66:
#         break
#     print(n)

# else:
#     print("ok")

from colorama import Fore, Back, Style
from exercise1_utils import add_new_student, show_all_students, search
all_students = []

menu_str = f'''
{Fore.YELLOW+Back.BLUE}{"To Exit ":<30}{"-> 0": >10}{Style.RESET_ALL}
{Fore.RED+Back.GREEN}{"To Add new Student ":<30}{"-> 1": >10}{Style.RESET_ALL}
{Fore.BLUE+Back.RED}{"To Show All Student ":<30}{"-> 2": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To delete a Student ":<30}{"-> 3": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To Search a Student ":<30}{"-> 4": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To Update a Student ":<30}{"-> 5": >10}{Style.RESET_ALL}
'''


status = True
while status:
    print(menu_str)
    user_input = input('> ')
    if user_input == '0':
        print("bye")
        exit()
    elif user_input == "1":
        add_new_student(all_students)
    elif user_input == "2":
        show_all_students(all_students)
    # TODO search and update

    elif user_input == "4":
        name = input('Enter syudent`s name: ')
        print(search(name, all_students))
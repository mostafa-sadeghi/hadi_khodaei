from colorama import Fore, Back, Style
from exercise1_utils import add_new_student, show_all_students, search, delete_student, update, multiple_search
all_students = []

menu_str = f'''
{Fore.YELLOW+Back.BLUE}{"To Exit ":<30}{"-> 0": >10}{Style.RESET_ALL}
{Fore.RED+Back.GREEN}{"To Add new Student ":<30}{"-> 1": >10}{Style.RESET_ALL}
{Fore.BLUE+Back.RED}{"To Show All Student ":<30}{"-> 2": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To delete a Student ":<30}{"-> 3": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To Search a Student ":<30}{"-> 4": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To Update a Student ":<30}{"-> 5": >10}{Style.RESET_ALL}
{Fore.YELLOW+Back.BLUE}{"To Update a multiple search ":<30}{"-> 6": >10}{Style.RESET_ALL}
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
    elif user_input == "3":
        name = input('Enter a name to delete:> ')
        delete_student(name, all_students)

    elif user_input == "4":
        name = input('Enter student`s name: ')
        print(search(name, all_students)[2])

    elif user_input == "5":
        name = input('Enter student`s name: ')
        what_to_update = input(
            'Which one you want to change? ("family", "name", "age", "course"): ')
        update(name, what_to_update, all_students)
    elif user_input == "6":
        name = input('Enter student`s name: ')
        res = multiple_search(name, all_students)

        course_name = input(
            'Enter the course name: (python, java , javascript) ')
        course_stu = []
        for student in res:
            if course_name == student["course"]:
                course_stu.append(student)

        print(course_stu)

def add_new_student(all_students):
    student = {}
    student['name'] = input('enter student`s name: ')
    student['family'] = input('enter student`s family: ')
    student['age'] = int(input('enter student`s age: '))
    student['course'] = input(
        'Enter your course name (python, java , javascript) ')
    all_students.append(student)


def show_all_students(all_students):
    for student in all_students:
        print(
            f"{student['name']}   {student['family']}   {student['age'] }   {student['course']}")


def search(name, all_stu):

    for i in range(len(all_stu)):
        if name == all_stu[i]["name"]:
            return True, i, all_stu[i]["course"]

    return False, -10, ""


def delete_student(name, students):
    result = search(name, students)
    if result[0]:
        del students[result[1]]


def update(n, w, l):
    result = search(n, l)
    if result[0]:
        print(f"change {w} to What?")
        user_input = input('> ')
        l[result[1]][w] = user_input


def multiple_search(name, all_stu):
    temp_list = []
    for i in range(len(all_stu)):
        if name == all_stu[i]["name"]:
            temp_list.append(all_stu[i])
    return temp_list
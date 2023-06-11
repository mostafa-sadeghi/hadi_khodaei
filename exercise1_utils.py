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
    for st in all_stu:
        if name == st["name"]:
            return st["course"]

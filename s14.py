# all_students = []


# student = {}
# name = input('Enter your name: ')
# student["name"] = name
# cancel_or_commit = input("Are you Sure? (y | n) ")
# if cancel_or_commit == "y":
#     all_students.append(student)



# def f(x):
#     x = x + 1
#     print(f"in f(x) : x =", x)
#     return x

# x = 3
# z = f(x)
# print(f"z = {z}")
# print(f"x outside of f {x}")



# def is_even(i):
#     # return i % 2 == 0
#     print(i % 2 == 0)


# print(is_even(4))

# TODO  
# یک تابع بنویس که نمره دانشجویی را بگیرد
# اگر نمره از 50 کمتر باشد
# F
# اگر نمره از 89 بیشتر باشد
# A+
# اگر نمره بین 85 و 89 باشد
# A
# اگر نمره بزرگتر از 79 
# A-

# 85 - 79  => B+
# 69 - 84  => B-
# ....
# C
# D

# تابعی بنویس که یک لیست از اعداد را دریافت نماید
# و اگر لیست صعودی هست
# True
# در غیر اینصورت 
# False 
# برگرداند

# [1,2,3,4,5] => True
# [1,2,0,4,5] => False
# [5,4,3,2,1] => False

# تمرین:
# یک تابع بنویس یک لیست بگیرد و لیست را نصف کند
# تابع یک پارامتر به نام out 
#دارد
# [1,2,3,4,    5,6,7,8]  
# out = True => [1,5,2,6,3,7,4,8]
# out = False => [5,1,6,2,7,3,8,4]

def my_func(numbers, out):
    pass

my_func([1,2,3,4,5,6,7,8], True)

# تمرین 
# تابعی بنویس که یک عدد بگیرد و در صورتی که رقم های آن عدد فرد باشد
# True
# در غیر اینصورت 
# False 
# برگرداند

# 8   =>   False
# 1357913579   =>   True
# 42   =>   False
# 71358   =>   False
# 0   => False


# def func_a():
#     print('inside func_a')

# def func_b(y):
#     print('inside func_b')
#     return y

# def func_c(z):
#     print('inside func_c')
#     return z()

# print(func_a())
# print(5 + func_b(2))
# print(func_c(func_a))


# def login():
#     global x
#     x += 1
#     print(f"login attemp {x}")

# x = 0
# login()
# login()
# login()


# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =', x)
#     h()
#     return x

# x = 3
# z = g(x)
# print("z =",z)
# print("x =",x)

def print_name(fname, lname, reverse):
    if reverse:
        print(lname , ', ', fname)
    else:
        print(fname , ', ', lname)

print_name("sara", "blalal", False)
print_name("sara", "blalal", True)
print_name("sara", "blalal", reverse=True)
print_name(fname="sara", lname="blalal", reverse=True)
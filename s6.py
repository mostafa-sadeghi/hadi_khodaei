# total = 0

# for i in range(100):
#     total += i

# print(total)

# import sys

# numbers = [1,2,3,4,5,6,7,8,9,0]

# print(sys.getsizeof(numbers))
# n = 12
# print(sys.getsizeof(n))

# name = input('enter a name: ')
# print(name[::-1])
# for i in range(len(name)-1,-1,-1):
#     print(name[i], end='')
# for i in range(1,len(name)+1):
#     print(name[len(name)-i],end='')


# while loop

# for i in range(10):
#     print(i, end="")

# i = 0
# while i < 10:
#     print(i, end='')
#     print("")
#     i += 1  # i = i + 1


# quit = "n"
# while quit == "n":
#     quit = input('Do you want to quit? ')

# done = False
# while not done:
#     quit = input('Do you want to quit? ')
#     if quit == "y":
#         done = True


# for i in range(10):
#     if input('> ').lower().startswith("y"):
#         break
#     print(i, "another step...")
# for i in range(10):
#     if input('> ').lower().startswith("y"):
#         continue
#     print(i, "another step...")


# if 3 < 4:
#     pass


import random
# for i in range(10):
#     print(random.random())

# print(random.randint(1,10))
# print(random.randrange(1,10))

# ACTIONS = ("paper", "rock","scissors")
# random_index = random.randrange(len(ACTIONS))
# print(ACTIONS[random_index])

# print(random.choice(ACTIONS))

# while loop    for loop    input    if elif else    random    datatypes    print

'''
بازی سنگ کاغذ قیچی
تا زمانی که بازیکن بخواهد بازی ادامه داشته باشد
بازیکن ها : ما و کامپیوتر
score bord  ############
##########################
player score :          23
computer score:         12
###########################

'''


x = 13

if x == 12:
    print("x == 12")

elif x == 13:
    print("x == 13")

else:
    print("some thing else")

# exercise 2 :
'''
برنامه ای بنویسی که نام و سن فردی را از ورودی دریافت نماید
و اگر سن او کمتر از هشت بود
kid
اگر سن او بین هشت و سیزده بود
junior
اگر سن اول بین سیزده و هجده بود
teenager
در غیر اینصورت 
adult

'''
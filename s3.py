# print('* ' * 10)
# print('* ' + str(10))

# shopping_list = 'banana apple pen mashroom'
# print(shopping_list[0])
# shopping_list = ['banana', 'apple', 'pen', 'mashroom']
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
# print(shopping_list)
# print(f'my shoppinglist`s length is:{len(shopping_list)}')

# shopping_list.append('potato')
# print(shopping_list)
# print(f'my shoppinglist`s length is:{len(shopping_list)}')

# numbers = [22,33,45,67]
# result = numbers[0] + numbers[1] + numbers[2] + numbers[3]
# print(f'{numbers[0]} + {numbers[1]} + {numbers[2]} + {numbers[3]} = {result}')

# print(sum(numbers))

# name = "reza"
# family = "rezaei"
# message = f"welcome {name} {family}"
# print(message)


# my_list = [1, 2, 3, "ali", ["a", "b"]]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[4][0])
# print(my_list[4][1])


# list1 = [1,2,3,4]
# list2 = [6,7,8]

# output_list = list1 + list2
# print(output_list)

# output = list1 * 5
# print(output)


# friends = []

# name1 = input('enter a name to add: ')
# friends.append(name1)

# name2 = input('enter a name to add: ')
# friends.append(name2)

# name3 = input('enter a name to add: ')
# friends.append(name3)

# print(friends) 

# name_del = input('enter a name to del: ')
# friends.remove(name_del)
# print(friends) 

# del friends[0]
# print(friends) 

number1 = int(input('enter a number: '))
number2 = int(input('enter a number: '))
result = number1 + number2
print(result)

# exercise 1 : برنامه ای بنویسید که سه عدد از ورودی دریافت نماید و در لیستی اضافه کند
# مجموع اعداد موجود در لیست را محاسبه کن و نمایش بده
# از لیست اعداد، آخرین عدد را حذف کن و لیست را مجددا نمایش بده
# مجموع اعداد لیست را پس از حذف عدد بار دیگر نمایش بده


numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[:3])
print(numbers[3:6])
# exercise :
# charcters = ['a','b','c','d','e','f','g','h']

# برش های زیر را از لیست بالا ایجاد کن
'''
['a','b']
['g','h']
['e','f','g']
['b','c','d','e']
'''

numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[::2])
# exercise : از لیست بالا اعداد فرد را نمایش بده

print(numbers[:2] + numbers[8:])
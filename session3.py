# import string
# def isPalindromic(s):

#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for char in s:
#             if char in string.ascii_lowercase:
#                 ans += char
#         return ans

#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])

#     return isPal(toChars(s))


# print(isPalindromic("Ab1ba"))


# import string


# def isPalindromic(s):

#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for char in s:
#             if char in string.ascii_lowercase:
#                 ans += char
#         return ans

#     def isPal(s):
#         global number_of_calls
#         number_of_calls += 1
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])

#     return isPal(toChars(s))
# number_of_calls = 0
# print(isPalindromic("Aa"))
# print(f"number of calls: {number_of_calls}")


# import circle

# print(circle.area(50))


# from circle import area
# print(area(50))


# from circle import area, circum

# print(area(50))


# def circum2():
#     return 400


# print(circum(23))


# file = open("my_file.txt", "w")
# for i in range(2):
#     name = input('enter a name: ')
#     file.write(name + '\n')

# file.close()

# try:
#     file = open("my_file.txt", "r")
#     for line in file:
#         print(line[:-1])

# except FileNotFoundError as ex:
#     file = open("my_file.txt", "w")
#     print(ex)
# except:

#     print("blalalal")
# finally:
#     file.close()


# a = int(input("enter a number: "))
# b = int(input("enter a number: "))


# try:
#     print(a/b)

# except:
#     print("undefined")

# else:
#     print("ELSE")
# finally:
#     print("FINALLY")


# with open("my_file.txt", "r") as f:
#     for line in f:
#         print(line[:-1])


# with open("my_file.txt", "a") as file:
#     for i in range(2):
#         name = input('enter a name: ')
#         file.write(name + '\n')

# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

#     return L


# print(applyToEach([1.2,2.3,4.5], int))
# print(applyToEach([1,2,4], float))
# print(applyToEach([-1,-2,4], abs))

# def applyFuns(L, x):
#     for f in L:
#         print(f(x))


# applyFuns([abs, int, float], 4)


# result = map(abs, [1, -2, 3, -4])
# for item in result:
#     print(item)


# def my_func(number):

#     return number*2


# result = map(my_func, [1, -2, 3, -4])
# for item in result:
#     print(item)


# def mul(a,b):
#     result = 0
#     while b>0:
#         result += a
#         b -= 1

#     return result

# print(mul(2,3))

"""
a * b = a + a + a + ..... + a
      = a + a + a + ...
      = a + a * (b-1)


"""


# def mul(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mul(a, b-1)


# print(mul(2, 3))

# n! = n * (n-1) * (n-2) * (n-3) * .... * 1


# def fact(n):
#     if n == 1:
#         return 1

#     else:
#         return n * fact(n-1)


# print(fact(50))

# def fact(n):
#     x  = 1
#     for i in range(1,n+1):
#         x *= i
#     return x

# print(fact(50))


def nonNegativeFloatValidation(prompt, errorMessage):
    number = input(prompt)
    float_number = float(number)
    if float_number > 0:
        return float_number
    else:
        print(errorMessage)
        return nonNegativeFloatValidation(prompt, errorMessage)


nonNegativeFloatValidation(
    "Enter a nonnegative float number: ", "you must enter a nonNegative float number")

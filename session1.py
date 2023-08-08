# def letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return "A+"
#     elif n > 84:
#         return "A"
#     elif n > 79:
#         return "A-"
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones >6:
#         adjust = "+"
#     else:
#         adjust = ""

#     return "DCB"[tens - 5] + adjust

# print(letter_grade(87))


# numbers1 = [1,2,3,4,5,6,7]
# numbers2 = [1,2,3,0,6,7]
# numbers3 = [8,7,6,4]

# def is_ascending(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             return False

#     return True

# print(is_ascending(numbers3))


# if out := true  -> output := [1,5,2,6,3,7,4,8]
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
# if out := false -> output := [5,1,6,2,7,3,8,4]
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]


def my_func(numbers, out=True):
    length_half = int(len(numbers)/2)
    new_numbers = []
    first_half = numbers[:length_half]
    second_half = numbers[length_half:]
    print("first half:", first_half)
    print("second half", second_half)
    for i in range(length_half):
        if out:
            new_numbers.append(first_half[i])
            new_numbers.append(second_half[i])

        else:
            new_numbers.append(second_half[i])
            new_numbers.append(first_half[i])

    return new_numbers


print(my_func(numbers1))
print(my_func(numbers1, False))

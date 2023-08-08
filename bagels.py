import random
import string
MAX_DIGITS = 3
MAX_GUESSES = 10


def make_secret_number():
    numbers = list(string.digits)
    random.shuffle(numbers)
    return ''.join(numbers[:MAX_DIGITS])


def user_help(guess, secret):
    if guess == secret:
        return "you are winner!!"

    help_list = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            help_list.append("Fermi")
        elif guess[i] in secret:
            help_list.append("Pico")

    if not len(help_list):
        return "Bagels"

    else:
        return " ".join(help_list)


message = f"""Welcome to Bagels Game:
You should guess a "{MAX_DIGITS}" digits number, and you have "{MAX_GUESSES}" times to guess it.
Pico        =>   One digit is correct but not in the right position,
Fermi       =>   One digit is correct and is in the right position,
Bagels      =>   No digit is correct
"""

print(message)

secret_number = make_secret_number()
# print("secret number:", secret_number)
print("secret numbet is generated!!!")
number_of_guesses = 1
while number_of_guesses < 11:
    print(f"guess # {number_of_guesses}")
    user_guess = ""
    while len(user_guess) != 3 or not user_guess.isdecimal():

        user_guess = input("enter a three digits number: ")

    help_result = user_help(user_guess, secret_number)
    print(help_result)
    if secret_number == user_guess:
        break

    number_of_guesses += 1

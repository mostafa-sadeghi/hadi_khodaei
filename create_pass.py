import string
from random import choices


def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if not pool:
        pool = string.ascii_letters
        

    return ''.join(choices(pool, k=length))
    
    # password = ''
    # for char in choices(pool, k=length):
    #     password += char

    # return password


print(create_password())

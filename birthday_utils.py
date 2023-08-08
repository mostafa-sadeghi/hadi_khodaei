import datetime
import random


def generate_birthdays(num_of_birthdays):
    """
    this function is used for generating numbers of birthdays
    :param num_of_birthdays:
    :return: a list of random birthdays
    """

    birthdays = []
    start_date = datetime.date(2022, 1,1)
    for i in range(num_of_birthdays):
        random_numbers_of_dates = datetime.timedelta(random.randint(0,364))
        birthday = start_date + random_numbers_of_dates
        birthdays.append(birthday)
    return  birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for i in range(len(birthdays) - 1):
        for j in range(i+1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]

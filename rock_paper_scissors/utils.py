from random import choice

from rock_paper_scissors.config import GAME_CHOICES, RULES


def get_user_choice(prompt):
    """
    This function is used for getting user choice between (r, p , s)
    :return: user_choice
    """
    user_choice = input(prompt)
    if user_choice not in GAME_CHOICES:
        return get_user_choice("input is not correct, please enter (r, p, s): ")

    return user_choice


def get_system_choice():
    return choice(GAME_CHOICES)


def find_winner(user_choice, system_choice):
    match = {user_choice, system_choice}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]




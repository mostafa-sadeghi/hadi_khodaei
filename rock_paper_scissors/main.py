from rock_paper_scissors.utils import get_user_choice, get_system_choice, find_winner


def play():
    result = {
        'user': 0,
        'system': 0
    }
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice("Enter your choice (r, p, s): ")
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        # TODO find the winner
        # show the winner and the scoreboard


import random


def play():
    permission = input("Do you want to play a game?(y/n): ").lower()
    if permission == "y":
        name = input("Please enter your name: ")
        print(f"Welcome {name} to a game of Rock, Paper, Scissors")
        players_choice = input(
            "Choose 'r' for Rock, 'p' for Paper or 's' for Scissors : ")
        computers_choice = random.choice(['r', 'p', 's'])

        if players_choice == computers_choice:
            return f"Sorry, {name}. It\'s a tie"

        if winning_rules(players_choice, computers_choice):
            return f"Congratulations {name}! You won"

        return f"You lost. Better luck next time, {name}"

    elif permission != 'n':
        return "Select a 'y' or 'n' next time"
    else:
        quit("Goodbye")


def winning_rules(player, computer):
    # Rules  r > s, s > p, p > r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'r') or \
            (player == 'p' and computer == 'r'):
        return True


print(play())

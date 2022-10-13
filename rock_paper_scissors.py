import random
import time

name = input('Enter your name: ')
print(f'Welcome {name}, to Game world :)')
print('')

time.sleep(1)
response = input('Do you want to play?(y/n): ').lower()

if response == 'n' or response == 'no':
    quit(f'Goodbye, {name}. Cowards are not welcomed here!')

else:
    print('')
    print('The Game begins!!!')

time.sleep(1)    

def play():
    print('Rules')
    print('--------------------')
    print('R is for Rock, P is for Paper and S is for Scissors')
    
    users_choice = input('Enter your choice: ').lower()
    computer_choice = random.choice(['r', 'p', 's'])

    while who_won is False:
        users_choice = input('Enter your choice: ').lower()
        computer_choice = random.choice(['r', 'p', 's'])

    if users_choice == computer_choice:
        print('That is a tie')

    
        pass
    elif who_won(users_choice, computer_choice):
        print('You won!')
    else:
        print(f'Sorry {name}, you lost')


# rules for the game
# r beats s, s beats p, p beats r
def who_won(player, opponent):
    if (player  == 'r' and opponent == "s") or (player  == 's' and opponent == "p") or (player  == 'p' and opponent == "r"):
        return True
    return False
      
    
play()
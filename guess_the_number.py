import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Type a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Guess too high!")

    print(
        f"Congratulations! {guess} is correct. You have successfully guessed the computer's number")


guess(50)

import time


t = input("Enter the time in seconds: ")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Lift off!')


countdown(int(t))


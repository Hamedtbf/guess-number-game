import random


def computer_guess(a, b):
    guess = random.randint(a, b)
    print(guess)
    return guess


min = 1
max = 99
while True:
    guess = computer_guess(min, max)
    user_input = input()
    while user_input != 'k' and user_input != 'b' and user_input != 'd':
        user_input = input()
    if user_input == 'k':
        max = guess - 1
        continue

    elif user_input == 'b':
        min = guess + 1
        continue
    else:
        break

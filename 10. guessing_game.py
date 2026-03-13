def guessing_game():
    while True:
        print('what is your guess?')
        guess = input()

        if guess == '42':
            print ('You correctly guessed it!')
            return False
        
# guessing_game()

import random

def guessing_game_random():
    number = random.randint(1,10)
    while True:
        print('what is your guess the number?')
        guess = int(input())
       

        if guess == number:
            print(f'You got it right!!. The number is {number}')
            return False
        elif guess > number:
            print(f'The number is  lower than {guess}')
        elif guess < number:
            print(f'The number is  higher than {guess}')

guessing_game_random()
        
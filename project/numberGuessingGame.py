# display welcome message
# think of a number between 1 to 100
# choose difficulty level, from the user
# easy: 10 attempts
# difficulty: 5 attempts
# get the number from user?
# check the number is equal,
    # if so, print win
    # else
    # if greater than 
    #   display greater than,
    #   reduce attempt count
    # if less than,
    #   display less than
    #   reduce attempt count
    # 
# repeat the steps


from random import *


def welcome():
    print('*****Welcome to number guessing game******')


def think_a_number():
    print('I am thinking a number between 1 to 100')
    return randint(0,101)

def level_of_difficulty():
    level = input("choose difficulty level? easy or hard ? :")
    if (level == 'easy'):
        return 10
    else:
        return 5

def level_counter(level):
    print('You have {} attempts remaining'.format(level))


welcome()
guessed_number = think_a_number()
level = level_of_difficulty()
level_counter(level)

while True:
    user_guessed = int(input('Make a guess: '))
    if user_guessed == guessed_number:
        print('You won !!!, your guess is right :)')
        break
    elif user_guessed > guessed_number:
        print('Your number is greater than my number')
        level -= 1
    else:
        print('Your number is less than my number')
        level -= 1
    if level == 0:
        level_counter(level)
        print('You lose :(, better luck nect time :)')
        print('My number is {}'.format(guessed_number))
        break



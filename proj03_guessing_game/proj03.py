# Name:
# Date:


import random

""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


#Mode Variables
mode = input("Which mode would you like? (easy, medium, hard, extreme)")
if mode == "easy":
    num_range = 10
elif mode == "medium":
    num_range = 25
elif mode == "hard":
    num_range = 50
elif mode == "extreme":
    num_range = 100
else:
    num_range = 1000


#Starter string + Variables
guess = input("Guess a number " + "1-" + str(num_range) + " or type 'exit' to end the game:")
guess_num = 1
rand_num = random.randint(1, num_range)
win = 0




#Loop for Game
while guess != "exit" and win == 0 and guess_num < 6:
    guess = int(guess)

    if guess == rand_num:
        print("Congrats you won the game!")
        win = 1
        print("You've guessed " + str(guess_num) + " times.")
    elif guess < rand_num:
        print("Your number is too low!")
        guess_num = guess_num + 1
        if win == 0 and guess_num == 6:
            print("YOU LOST! You reached 5 guesses. The random number was " + str(rand_num))

    else:
        print("Your number is too high!")
        guess_num = guess_num + 1
        if win == 0 and guess_num == 6:
            print("YOU LOST! You reached 5 guesses. The random number was " + str(rand_num))


    if win == 0 and guess_num < 6:
        guess = input("Guess a number " + "1-" + str(num_range) + " or type 'exit' to end the game:")






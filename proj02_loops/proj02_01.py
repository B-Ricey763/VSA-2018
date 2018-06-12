# Name:
# Date:

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21


#Number adding thing
num = int(input("Enter a number to sum, or 0 to indicate you are finished:"))
sum = 0
summ = 0


while num > 0:
    sum = sum + num
    num = int(input("Enter a number to sum, or 0 to indicate you are finished:"))
    summ = summ + 1



average = sum/summ

print("Your average is " + str(average))

""""#R/P/S
answer = input("Would you like to play?")

while answer == "Yes":
    p1_input = input("Rock, paper, scissors")
    p2_input = input("Rock, paper, scissors")

    if p1_input == "rock" and p2_input == "paper":
        print("Player 2 wins")
    elif p1_input == "rock" and p2_input == "scissors":
        print("Player 1 wins")
    elif p1_input == "paper" and p2_input == "rock":
        print("Player 1 wins")
    elif p1_input == "paper" and p2_input == "scissors":
        print("Player 2 wins")
    elif p1_input == "scissors" and p2_input == "rock":
        print("Player 2 wins")
    elif p1_input == "scissors" and p2_input == "Paper":
        print("Player 1 wins")
    else:
        print("It is a tie")
    answer = input("Would you like to play again?")"""













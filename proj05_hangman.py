# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()


#Variables
alpha = string.lowercase
num_guesses = 6
win = 0
blank_list = []
word = choose_word(wordlist)
word_letter = []
counter = 0
win_counter = 0
win1 = 0

#Word to Word List and Blank spaces to Blank list
for letter in word:
    word_letter.append(letter)

for letter2 in range(len(word_letter)):
    blank_list.append("_")

#starting string
print ("Welcome to Hangman! I am thinking of a word that is " + str(len(word_letter)) + " letters long.")

user_guess = raw_input("Guess a letter:")

if user_guess in word_letter:
    print("Good Guess")
else:
    print("Oops! That letter is not in my word!")
    num_guesses = num_guesses - 1




#Main loop
while win1 == 0 and num_guesses != 0:
    for letter1 in word_letter:
        if user_guess == letter1:
            blank_list[counter] = user_guess
        counter = counter + 1
    counter = 0
    print(" ".join(blank_list))
    alpha = alpha.replace(user_guess, "")
    print("Available letters:" + "".join(alpha))
    win = 0
    for letter5 in word_letter:
        if letter5 == blank_list[win_counter]:
            win = win + 1
        win_counter = win_counter + 1
    win_counter = 0
    if win == (len(word_letter)):
        win1 = win1 + 1

    print("You have " + str(num_guesses) + " guesses left")
    if win1 == 0:
        user_guess = raw_input("Guess a letter:")
    if user_guess not in word_letter:
        num_guesses = num_guesses - 1
        print("Oops! That letter is not in my word!")
    elif user_guess in word_letter:
        print("Good Guess!")
    if win1 == 1:
        print("You win!")























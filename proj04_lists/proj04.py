# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
#and write a program that prints out all the elements of the list that are less than 5.

"""for change_item in range(len(a)):
    if a[change_item] < 5:
        new_list.append(a[change_item])
print(new_list)"""





#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

"""sim_list = []


for sim_item1 in b:
        if sim_item1 in c and sim_item1 not in sim_list:
            sim_list.append(sim_item1)

print(sim_list)"""








#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
counter = 0

for letter in d:
    if letter == "a":
        d[counter] = "*"
    counter = counter + 1

print(d)


#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

word = input("Enter a word: ")
list = []
counter1 = 0
pali = 0

for letter1 in word:
    if letter1 != " ":
        list.append(letter1)



for letter2 in list:
    if (len(list))%2 == 0:
        if counter1 <= (len(list)):
            if list[0].lower() == list[-1].lower():
                list = list[1:-1]
    elif (len(list))%2 == 1:
        if counter1 <= (len(list)) and (len(list)) > 1:
            if list[0].lower() == list[-1].lower():
                list = list[1:-1]
    counter1 = counter1 + 1

if pali == (len(list)) or pali == (len(list)) - 1:
    print("Your word is a palindrone")
else:
    print("Your word is not a palindrone")
















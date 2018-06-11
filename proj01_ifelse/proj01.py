# Name:
# Date:

# proj01: A Simple Program



# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.


#name = input("What's your name?")
#grade = int(input("What grade are you in?"))
#print(name[0].upper() + name[1:].lower() + " will graduate in " + str(12 - grade) + " years.")


# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

#Variables for Dates
current_day = 11
current_month = 6

#Initial input
name = input("What is your name?")
birthday = int(input("When is your birthday?"))
birth_month = int(input("When is your birth month?"))

#Math for remaining months
if birth_month >= current_month:
    months_left = 12 - (birth_month - current_month)
elif birth_month < current_month:
    months_left = 12 - (current_month - birth_month)

#Math for remaining days
if birthday >= current_day:
    days_left = birthday - current_day
elif birthday < current_day:
    days_left = 30 - (current_day - birthday)
    months_left = months_left - 1

print(name + ", your next birthday is in " + str(days_left) + "days and " + str(months_left) + "months")



# If you complete extensions, describe your extensions here!

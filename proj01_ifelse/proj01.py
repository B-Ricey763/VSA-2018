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
current_day = 12
current_month = 6

#Initial input
name = input("What is your name?")
birthday = int(input("When is your birthday?"))
birth_month = str(input("What is your birth month?"))

#String to Number Change
if birth_month == "January":
    month_num = 1
elif birth_month == "February":
    month_num = 2
elif birth_month == "March":
    month_num = 3
elif birth_month == "April":
    month_num = 4
elif birth_month == "May":
    month_num = 5
elif birth_month == "June":
    month_num = 6
elif birth_month == "July":
    month_num = 7
elif birth_month == "August":
    month_num = 8
elif birth_month == "September":
    month_num = 9
elif birth_month == "October":
    month_num = 10
elif birth_month == "November":
    month_num = 11
else:
    month_num = 12

#Remaining months
if month_num >= current_month:
    months_left = 12 - (month_num - current_month)
elif month_num < current_month:
    months_left = 12 - (current_month - month_num)

#Remaining days
if birthday >= current_day:
    days_left = birthday - current_day
elif birthday < current_day:
    days_left = 30 - (current_day - birthday)
    months_left = months_left - 1

#Final String
print(name[0].upper() + name[1:].lower() + ", your next birthday is in " + str(days_left) + " days and " + str(months_left) + " months.")


# If you complete extensions, describe your extensions here!

current_year = 2018

name = input("What is your name?")
birth_date = int(input("What year were you born in?"))

age = current_year - birth_date

if age < 13:
    print("You can only see G and PG movies.")
elif 13 <= age < 17:
    print("You can see G, PG, and PG-13 movies.")
else:
    print(name[0].upper() + name[1:].lower() + "can see G, PG, PG-13, and R movies")


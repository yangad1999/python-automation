import datetime
import os

# if current hour is less than 12 = "Good Morning"
# if current hour between 12 to 5 = "Good Afternoon"
# if current hour greter than 5 then = "Good Evening"

# if / match

os.system("cls")
currentHour = 8  #datetime.datetime.now().hour

# operator +, -, *, /, % =
# conditional operators == > >= < <= != not or and
# Python is idented language

########### Style 1 ##############

# if currentHour < 12:
#     print("Good Morning")
#     print("Welcome to eClerx")
#     print("Please have a seat")

# if currentHour >= 12 and currentHour < 17:
#     print("Good Afternoon")
#     print("Welcome to eClerx")
#     print("Did you eat lunch")

# if currentHour > 17:
#     print("Good Evening")
#     print("Welcome to eClerx")
#     print("Have a cup of tea")
    
########### Style 2 ##############

# if currentHour < 12:
#     print("Good Morning")
#     print("Welcome to eClerx")
#     print("Please have a seat")
# elif currentHour >= 12 and currentHour < 17:
#     print("Good Afternoon")
#     print("Welcome to eClerx")
#     print("Did you eat lunch")
# elif currentHour > 17:
#     print("Good Evening")
#     print("Welcome to eClerx")
#     print("Have a cup of tea")

########### Style 2 ##############

if currentHour < 12:
    print("Good Morning")
    print("Welcome to eClerx")
    print("Please have a seat")
elif currentHour < 17:
    print("Good Afternoon")
    print("Welcome to eClerx")
    print("Did you eat lunch")
else:
    print("Good Evening")
    print("Welcome to eClerx")
    print("Have a cup of tea")

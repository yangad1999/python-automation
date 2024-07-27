import os

os.system("cls")
currentYear = input("Please enter year: ")
currentYear = int(currentYear)
reminder = currentYear % 4

if reminder == 0:
    centuryYear = currentYear % 100
    if centuryYear == 0:
        fourCenturyYear = currentYear % 400
        if fourCenturyYear == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Yeer")
else:
    print("Not Leap Yeer")


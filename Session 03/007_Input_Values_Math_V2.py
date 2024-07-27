import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear_screen()
    print('#' * 80)
    print('Python Calculator')
    print('#' * 80)

    result = None
    nextvalue = None
    operationtype = None

    while True:
        result_input = input("Input First Value: ")
        if result_input.isdigit():
            result = int(result_input)
            break
        else:
            print("Please input a valid number.")

    while True:
        nextvalue_input = input("Input Second Value: ")
        if nextvalue_input.isdigit():
            nextvalue = int(nextvalue_input)
            break
        else:
            print("Please input a valid number.")

    while True:
        operationtype = input("Select Operation:\nType 1 for addition\nType 2 for subtract\nType 3 for multiply\nType 4 for divide: ")
        if operationtype in ["1", "2", "3", "4"]:
            break
        else:
            print("Please type a number between 1 to 4.")

    operationtype = int(operationtype)

    if operationtype == 1:
        print(f"Result: {result} + {nextvalue} = {result + nextvalue}")
    elif operationtype == 2:
        print(f"Result: {result} - {nextvalue} = {result - nextvalue}")
    elif operationtype == 3:
        print(f"Result: {result} * {nextvalue} = {result * nextvalue}")
    elif operationtype == 4:
        if nextvalue != 0:
            print(f"Result: {result} / {nextvalue} = {result / nextvalue}")
        else:
            print("Error: Division by zero.")
    else:
        print("Unexpected operation type. Please type numbers between 1 to 4.")

    quit_input = input("\nDo you want to quit (y/n)? ")
    if quit_input.lower() == 'y':
        break

print("Exiting Python Calculator. Goodbye!")

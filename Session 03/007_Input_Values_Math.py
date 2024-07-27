import os

if os.name == 'nt': os.system('cls')
else: os.system('clear')

print('#' * 80)
print('Python Calculator')
print('#' * 80)

result = None
nextvalue = 0
operationtype = 0

# Operations
# - Addition
# - Subtration
# - Multiplication
# - Division

result = input("Input First Value: ")
nextvalue = input("Input Second Value: ")
#print("Select Operation: Type 1 for addition, type 2 for subtract, type 3 for multipy, type 4 for divide")
operationtype = input("Select Operation:\nType 1 for addition\nType 2 for subtract\nType 3 for multipy\nType 4 for divide: ")

result = int(result)
nextvalue = int(nextvalue)

if operationtype == "1":
    print(result + nextvalue)
elif operationtype == "2":
    print(result - nextvalue)
elif operationtype == "3":
    print(result * nextvalue)
elif operationtype == "4":
    print(result / nextvalue)
else:
    print("Please type numbers between 1 to 4")
 
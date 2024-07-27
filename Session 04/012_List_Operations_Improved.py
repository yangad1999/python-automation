import os

product_list = []

def printlist(title):
    os.system("cls")
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)
    
    for product in product_list:
        print(product)

def readproductfile():
    with open('products.csv', 'r') as file:
        next(file)
        
        for line in file:
            product_list.append(line.strip())

def saveproductfile():
    with open('products.csv', 'w') as file:
        file.write("Product\n")  # Writing the header
        for product in product_list:
            file.write(product + "\n")

readproductfile()
printlist("Product List")

while True:
    
    while True:
        operation = input("Press A to Add Product, Press R to Remove Product, Press Q to Quit: ")
        if operation in ["A", "R", "Q"]:
            break
        else:
            print("Enter Valid Value")
            
    if operation == "A":
        
        while True:
            product = input("Please Enter Product: ")
            product = product.strip()
            if len(product) > 1:
                break
            else:
                print("Please Enter product properly")
            
        product_list.append(product)
        printlist(f"Product is added: {product}")
        saveproductfile()
        
    elif operation == "R":
        
        while True:
            product = input("Please Enter Product: ")
            product = product.strip()
            if len(product) > 1:
                if product in product_list:
                    break
                else:
                    print("Product is not in list")
            else:
                print("Please Enter product properly")
        
        
        product_list.remove(product)       
        printlist(f"Product is removed: {product}")
        saveproductfile()
        
    elif operation == "Q":
        print("Thank you using our tool, Good Bye for now")
        break
    
        
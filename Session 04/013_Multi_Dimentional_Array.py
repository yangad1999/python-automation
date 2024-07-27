
product_list = [
    {"Name" : "Maggi Instant Noodles", "Price" : 20}, 
    {"Name" : "Parle-G Biscuits", "Price" : 5},
    {"Name" : "Tata Salt", "Price" : 30},
    {"Name" : "Amul Butter", "Price" : 50},
    {"Name" : "Kissan Fruit Jam", "Price" : 70},
    {"Name" : "Aashirvaad Atta", "Price" : 100},
    {"Name" : "MDH Masala Packets", "Price" : 20},
    {"Name" : "Fortune Sunflower Oil", "Price" : 120},
    {"Name" : "Haldiram's Namkeen", "Price" : 50},
    {"Name" : "Nestlé Milkmaid	", "Price" : 120},
    ]

def show_product_list(title):
    print("-" * 80)
    print(title)
    print("-" * 80)

    for product in product_list:
        print(product["Name"], product["Price"])
        
show_product_list("Initial Product List")

product_list.append({"Name" :  "Maggi Masala", "Price": 10})
product_list.append({"Name" :  "Amul Shrikhand", "Price": 95})
show_product_list("Added 2 Proudcts")

product_list.sort(key=lambda prd: prd["Name"])
show_product_list("Sorted Proudcts by Name")

product_list.sort(key=lambda prd: prd["Price"])
show_product_list("Sorted Proudcts by Price")

product_list.sort(key=lambda prd: prd["Price"], reverse=True)
show_product_list("Sorted Proudcts by Price Descending")

for product in product_list:
    if product["Name"] == "Amul Butter":
        product_list.remove(product)
show_product_list("Show Proudcts after removing")


for product in product_list:
    if product["Name"] in ["Tata Salt", "Aashirvaad Atta"]:
        product_list.remove(product)
show_product_list("Show Proudcts after removing")

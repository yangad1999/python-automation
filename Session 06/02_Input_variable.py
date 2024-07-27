import os
os.system('cls')

product_name = input("Enter product name:-")
product_rate = float(input("Enter product rate:-"))
product_discount_percentage = float (input("Enter product discount:-"))
product_quantity = int (input("Enter product quantity:-"))

total_product_cost = product_rate * product_quantity
total_discount_amount = total_product_cost * product_discount_percentage / 100
grand_total = total_product_cost - total_discount_amount

print('=' * 80)
print(' ' * 36, 'Invoice')
print('=' * 80)
print('Product Name:', product_name)
print('Product Rate:', product_rate)
print('Product Discount:', product_discount_percentage)
print('Product Quantity:', product_quantity)
print('-' * 80)
print(f'Total: {total_product_cost:.2f}')
print(f'Discount: {total_discount_amount:.2f}')
print(f'Grand Total: {grand_total:.2f}')
print('=' * 80)

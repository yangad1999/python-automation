########## Rules ##########

# 01 - You dont have to declare variable types
print('Example 01')
value01 = 10
value02 = 50
total = value01 + value02
print(total)

# You can define the variable type
product_qty : int = 10
product_price : float = 50.6

# 02 - Variable type can be changed anytime
print('Example 02')
value01 = 10
value02 = 50
print(type(value01))
value01 = "Ten"
value02 = "Fourty"
print(type(value01))
total = value01 + value02
print(total)

# 03 While declaring integer you can define any big number
print('Example 03')
population = 100
population = 1000000
population = 1000000000
population = 1000000000000
population = 1000000000000000
population = 1000000000000000000
population = 1000000000000000000000
population = 1000000000000000000000000

print(population * 25)

# 04 For Big Numbers you define under score for understanding value of number
print('Example 04')

profit = 5_442_525_511_742
loss = 3_545_125_524_441
print(profit - loss)

# 05 You can perfor calculation between float and int and output will be converted to float
print('Example 05')
numer_of_shares = 2510
share_price = 54.65
total_price = numer_of_shares * share_price
print(total_price)
print(type(total_price))


# 06 For string variables you can either use double or single quote, both are allowed
print('Example 05')

customer_name = "Deepak LD"
address_01 = "45, Darshana Bldg"
address_02 = 'Veer Savarkar Road'
city = 'Mumbai'

print(customer_name, address_01, address_02, city)

# 07 In boolean only two values are allowed

customer_name = "Pravin"
city = 'Pune'
is_married = True
is_manager = False
age = 29
is_mature = (age > 18)
print(type(is_mature))

# 08 NoneType doesnt hold any memory and value
count = None
count = 1


# 09 variable names must not be python keyword

# False
# None
# True
# and
# as
# assert
# async
# await
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield

# Receipts for Lovely Loveseats
"""
In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.
"""
# Adding In The Catalog
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00

# create stylish seat 
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylish_settee_description = 180.50

# create new item
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15

# calculation
sales_tax = 0.088

# Our First Customer
customer_one_total = 0
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description 
customer_one_total += lovely_loveseat_price + luxurious_lamp_price 

# sales tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print('Customer One Items:')
print(customer_one_itemization)

print('Customer One Total:')
print(customer_one_total)


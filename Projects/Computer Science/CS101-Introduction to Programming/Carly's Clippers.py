# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:11:43 2022

@author: hotty
"""

# Prices and Cuts:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print('Average Haircut Price:')
print(average_price)

new_prices = [element - 5 for element in prices]
print(new_prices)

# Revenue:
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue:', total_revenue)

# average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30 ]
print(cuts_under_30)
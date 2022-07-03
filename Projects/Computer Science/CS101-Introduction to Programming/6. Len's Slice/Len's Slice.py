# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:05:45 2022

@author: hotty
"""
# Len's Slice

# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your 
# knowledge of Python lists to organize some of your sales data.

# Make Some Pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 5, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print('We sell', num_pizzas, 'different kinds of pizza!')

pizza_and_prices = [[2,	"pepperoni"], [6,	"pineapple"], [1, "cheese"], [3,"sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorting and Slicing Pizzas
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
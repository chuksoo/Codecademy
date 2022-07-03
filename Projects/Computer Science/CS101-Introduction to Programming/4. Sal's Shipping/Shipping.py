# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 23:18:50 2022

@author: hotty
"""

# Sal's Shipping
weight = 41.5

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
cost = cost_ground
print(f'Cost of ground shipping:', '$ {}'.format(cost))

# Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight <= 6:
  cost_drone = weight * 9.0 + 0
elif weight <= 10:
  cost_drone = weight * 12.0 + 0
else:
  cost_drone = weight * 14.25 + 0
print(f'Cost of Drone shipping:', '$ {:.2f}'.format(cost_drone))
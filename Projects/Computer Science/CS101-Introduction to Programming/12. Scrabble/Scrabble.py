# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:02:01 2022

@author: hotty
"""
# Scrabble

# In this project, you will process some data from a group of friends playing scrabble. 
# You will use dictionaries to organize players, words, and points.

# Build your Point Dictionary
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)

# Score a Word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

# Score a Game
player_to_words = {"BLUE": ['EARTH', 'ERASER', 'ZAP'], "TENNIS": ['EYES', 'BELLY', 'COMA'], "EXIT": ['MACHINE', 'HUSKY', 'PERIOD']}

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
 
for element in oscars:
  print(element)
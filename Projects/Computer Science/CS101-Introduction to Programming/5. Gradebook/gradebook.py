# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:00:16 2022

@author: hotty
"""

# Gradebook

# You are a student and you are trying to organize your subjects and grades using Python. 
# Let’s explore what we’ve learned about lists to organize your subjects and scores.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create Some Lists: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics",	98], ["calculus",	97], ["poetry",	85], [
"history",	88]]
print(gradebook)

# Add More Subjects:
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modify The Gradebook:
gradebook[-1][-1] = 93 + 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

# One Big Gradebook!
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
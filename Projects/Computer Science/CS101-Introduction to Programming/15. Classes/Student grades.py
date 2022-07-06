# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:30:47 2022

@author: Chukwuemeka Okoli
"""

# define class `Student`
class Student:
    # add a constructor for `Student`
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    
    # add_grade() method
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
        else:
            print('Do nothing')

# create a `Grade` class
class Grade:
    minimum_passing = 65
    
    # give `Grade` a constructor
    def __init__(self, score):
        self.score = score

# create instance of class student
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:30:47 2022

@author: Chukwuemeka Okoli
"""

# create a `Grade` class
class Grade:
    minimum_passing = 65
    
    # give `Grade` a constructor
    def __init__(self, score):
        self.score = score
    def is_passing(self):
        if self.score >= Grade.minimum_passing:
            return True
        return False     

# define class `Student`
class Student:
    # add a constructor for `Student`
    def __init__(self, name, year):
 	    self.name = name
 	    self.year = year
 	    self.grades = []
         
    # add_grade() method
    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)
        else:
            return
        
    # add get_average() method
    def get_average(self):
        s = 0
        for student in self.grades:
            s += student.score
        return s/len(self.grades)
    
# create instance of class student    
roger = Student("Roger van der Weyden",10)    
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder",8)
x = Grade(65)    
print(pieter.add_grade(x))
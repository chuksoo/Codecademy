# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 23:07:52 2022

@author: hotty
"""

class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here - Q.1
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    # since using class variables here, use self keyword - Q.3
    estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi + 425*self.num_of_children + 24000*self.smoker - 12500
    print("{}'s estimated insurance costs is {} dollars".format(self.name, estimated_cost))

  # create an update_age() method - Q.5
  def update_age(self, new_age):
    self.age = new_age
    print("{} is now {} years old.".format(self.name, self.age))
    # Call the estimated_insurance_cost() method in update_age() - Q.7
    self.estimated_insurance_cost()

  # define a new method called update_num_children() - Q.8
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    #add control flow - Q.10
    if self.num_of_children == 1:
      print("{} has {} child.".format(self.name, self.num_of_children))
    else:
      # add print statement - Q.9
      print("{} has {} children.".format(self.name, self.num_of_children))
    # Call the estimated_insurance_cost() method in update_age() - Q.11
    self.estimated_insurance_cost()

  # method that uses dictionary to store patient variables - Q.12
  def patient_profile(self):
    patient_information = {}
    patient_information['Name'] = self.name
    patient_information['Age'] = self.age
    patient_information['Sex'] = self.sex
    patient_information['BMI'] = self.bmi
    patient_information['Number of Children'] = self.num_of_children
    patient_information['Smoker'] = self.smoker
    return patient_information


# create instance variable called 'patient1' - Q.2
patient1 = Patient('John Doe', 25, 1, 22.2, 0, 0)
print(patient1.name)  
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker) 

# use patient1 instance variable to test - Q.4
patient1.estimated_insurance_cost()

# test update_age() method - Q.6
patient1.update_age(26)

# test the num_new_children method
patient1.update_num_children(1)

# call the method patient_profile() - Q.13
print(patient1.patient_profile())


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:56:42 2023

@author: Nico
"""

## Class should be capitalized

class Animal():
    def __init__(self,region,animal_type,color,lethal):
        self.region = region 
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal
        
    
    def animal_bio(self):
        print(f"This is a {self.color} {self.lethal} {self.animal_type} which lives in {self.region}.")
        
        

## Do not hava additionnal properties
class Clinic(Animal):
    def animal_info(self):
        print(f"{self.animal_type},{self.region}.")
        
    def search(self,animals,region):
        for animal in animals:
            if animal.region == region:
                print(animal.animal_type)


Animal_list = []
n = input("How manay animals?")
for _ in range(int(n)):
    
    region = input("region:")
    animal_type = input("animal_type:")
    color = input("color:")
    lethal = eval(input("lethal:"))
    
    animal = Animal(region,animal_type, color, lethal)
    Animal_list.append(animal)
    
clinic = Clinic("Asia","tiger","orange",True)
clinic.animal_bio()
clinic.animal_info()
clinic.search(Animal_list,'USA')
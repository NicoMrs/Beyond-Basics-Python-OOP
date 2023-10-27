# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 07:42:48 2023

@author: Nico
"""

class Superhero():
    def __init__(self,name,power):
        self.name = name
        self.power = power
        
    def use_power(self):
        print(f"{self.name} uses {self.power}")
        
    def intro(self):
        print(f"name: {self.name},  power: {self.power}")
    
    def calculate_power(self):
        print(len(self.power))
        
        
class FlyingSuperhero(Superhero):
    
    def __init__(self,name,power,flying_speed):
        super().__init__(name,power) # initiate parent class
        self.flying_speed = flying_speed
        
    def use_power(self):
        print(f"{self.name} uses {self.power} at {self.flying_speed} mph")
    
    def calculate_flying_distance(self,flight_time):
        print(f"{flight_time*self.flying_speed}.")

batman = Superhero("batman", "strength")
batman.use_power()
batman.intro()
batman.calculate_power()

print()

starwing = FlyingSuperhero("starwing", "strength", "500")
starwing.use_power()
starwing.intro()
starwing.calculate_power()
starwing = starwing.calculate_flying_distance(2)
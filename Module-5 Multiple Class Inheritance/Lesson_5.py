# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:51:21 2023

@author: Nico
"""

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    
class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_cap = battery_capacity
        
    def charge(self):
        return self.battery_cap
    
    def get_elec_range(self):
        return self.battery_cap*5
    
class GasCar:
    def __init__(self, fuel_capacity):
        self.fuel_cap = fuel_capacity
        
    def refuel(self):
        return self.fuel_cap
    
    def get_fuel_range(self):
        return self.fuel_cap*20
    
    
class Hybrid(Vehicle, ElectricCar,GasCar):
    def __init__(self, make, model, year, battery_capacity, fuel_capcity):
        Vehicle.__init__(self,make, model, year)
        ElectricCar.__init__(self,battery_capacity)
        GasCar.__init__(self,fuel_capcity)


car = Hybrid("Toyota", "Prius", 2023,5,40)
battery_capacity = car.charge()
elec_range = car.get_elec_range()
fuel_range = car.get_fuel_range()

print(f"{battery_capacity} kwh")
print(f"{elec_range} km")
print(f"{fuel_range} km")
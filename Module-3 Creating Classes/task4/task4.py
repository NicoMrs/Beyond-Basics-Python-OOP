# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:39:59 2023

@author: Nico
"""

class Travel():
    
    def __init__(self,country,month,travel_type):
        self.country = country.lower()
        self.month = month.lower()
        self.travel_type = travel_type.lower()
        self.costs = []
        

    def trip_info(self):
        
        winter_months = ['october','november','december','january', 'february', 'march' ]
        summer_months = ['april', 'may', 'june', 'july', 'august','september']
                         
        
        if self.month in winter_months:
            print('This is a winter travel, travel type: {}'.format(self.travel_type))
        elif self.month in summer_months:
            print('This is a summer travel, travel type: {}'.format(self.travel_type))
        else:
            print('not a month')
            
    def list_inspection(self):
        n = sum([cost<10 for cost in self.costs])
        return n
    
    def calc_cost(self,cost):
        self.costs.append(cost)
        
        more_cost = 'y'
        
        while more_cost == 'y':
            
            more_cost = input("Any additionnal cost (y/n)?:")
            if more_cost.lower() != 'y' : 
                break
            
            self.costs.append(int(input("Enter cost :")))
            print('Updated price {}'.format(sum(self.costs)))
            
            
        if sum(self.costs) < 500 : 
            print("Low Budget")
        elif 500 < sum(self.costs) < 1500:
            print("Enjoy a flight to anywhere!" )
        else:
            print("Luxury trip!")
            
            
        if self.list_inspection() > 10:
            print("Price needs to be adjusted")
            print("Updated price {}".format(sum(self.costs) + self.list_inspection()))
        

            
            
    
travel = Travel('France', 'March', 'buisness')
travel.trip_info()
travel.calc_cost(50)
print(travel.costs)



            
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 07:43:25 2023

@author: Nico
"""

#### COMPOSITION

class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.pay*12) + self.bonus
    
        
    
## Salary is contained in Employee    
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay,bonus) #class composition 
        
    def total_salary(self):
        return self.obj_salary.annual_salary()
        
        
emp = Employee('max', 25, 15000 , 10000)
print(emp.total_salary())


#### AGGREGATION

class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.pay*12) + self.bonus
    
        
    
## Salary is contained in Employee    
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.obj_salary = salary
        
    def total_salary(self):
        return self.obj_salary.annual_salary()
        
salary = Salary(15000,10000)       
emp = Employee('max', 25,salary)
print(emp.total_salary())


        
        
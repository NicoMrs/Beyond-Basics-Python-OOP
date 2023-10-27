# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:07:04 2023

@author: Nico
"""


class Country():
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        
    def get_info(self):
        return {
                "Name" : self.name, 
                "Capital" : self.capital,
                "Population": self.population
                }
    
    
class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp
    
    # overriding of get_info from parent class
    def get_info(self):
        info = super().get_info()
        info["GDP"] = self.gdp
        return info
        

class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi
    
    # overriding of get_info from parent class
    def get_info(self):
        info = super().get_info()
        info["HDI"] = self.hdi
        return info


class WorldClass():
    def __init__(self):
        self.countries = [] # list of objects
        self.countries_dict = {} # countries dict
                
    def add_country(self,country):
        self.countries.append(country)
        self.countries_dict[country.name] = country.get_info()
        print(f"{country.name} has been added to the list of countries!")
        
    def get_country_info(self, name):
        if name not in self.countries_dict.keys():
            print("{} not found!".format(name))
        else:
            print(self.countries_dict[name])
            
            
    
usa = DevelopedCountry('USA', 'Washington', '330M', '23.32 tri')
china = DevelopingCountry('China', 'Pekin', '1.412B', '0.768')
india = DevelopingCountry('India', 'New Dehli', '1.408B', '0.633')

world = WorldClass()
world.add_country(usa)
world.add_country(china)
world.add_country(india)

print("\nCountries dictionnary")
print(world.countries_dict)

print("\nInformations")
world.get_country_info('India')


















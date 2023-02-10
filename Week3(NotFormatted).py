"""Lab: Gives a chance to practice implementing a class in Python.

Author: David Thomsen
Class: CSI-260
Assignment: Week 3 Lab
Due Date: February 9, 2023

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

"""

# Creates the class "Country", with variables:
# Area, Population, and Name.
class Country:
    area=0
    population=0
    name="Country"
    
    '''Creates the Country Class'''
    
    
    # The init function used for initialization.
    # Links the self.xxx of the country to the input. 
    def __init__(self,name,population,area):
        self.name = name
        self.population = population
        self.area = area
        
        '''Creates the init function'''
    
    # The function used for comparing Country.areas to see which is larger among the two.     
    def is_larger(self, other):
        if self.area > other.area:
            return(True)
            # print(self.name + " is the larger country" + '\n' )    
        elif self.area <= other.area:
            return(False)
            # print(self.name + " is the smaller country" + '\n' )
    
    '''If/Else checking to see which of the two is larger'''
    
    # This function calculates population density by dividing the population by the area.         
    def population_density(self):
        PopDens = (self.population / self.area)
        return(float(f'{PopDens:.4f}')) 
    
    '''Calculates and formates the population density'''        
       
    # Gives a general summary of the country. Shows all of the above information (as of submitting this).
    def summary(self):
        return(self.name + " has a population of " + str(self.population) 
              + " people and is " + str(self.area) + " square km. It therefore has a population density of "
              + format(self.population_density(), '.4f')  + " people per square km.")
    
    '''Summarizes all the previous stats.'''
  
  
  
  
  
  
  
KingdomOfAwesome = Country("Kingdom of Awesome", 10, 2)
Uraguay = Country("Uraguay", 999, 10109)
MakeBelieve = Country("MakeBelieve", 1000, 10000)

# print(Uraguay.name)
# print(Uraguay.population)
# print(Uraguay.area)

# Uraguay.is_larger(MakeBelieve)
print(Uraguay.population_density())
print(KingdomOfAwesome.summary())
# Uraguay.summary()


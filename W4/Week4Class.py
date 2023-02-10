import math

class Pizza:
    #declare class variables at the top
    pizzas_made = 0
    
    def __init__(self, diameter, ingredients):
        #define instance variables
        self.radius = diameter/2
        self.ingredients = ingredients
        self.__class__.pizzas_made +=1
        
    def __repr__(self):
        return(f'Pizza({self.radius !r},'f'{self.ingredients!r}')
        
        
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return (r**2 + math.pi)
        
    
    @classmethod
    def margherita(cls):
        print("making a margherita..")
        return cls(16, ["Mozzerella", "Tomatoes"])
    @classmethod
    def hawaiian(cls):
        print("making a hawaiian..")
        return cls(16, ["Mozzerella", "Tomatoes", "Pineapple", "Ham"])
    @classmethod
    def made(cls):
        return(cls.pizzas_made)
 
        
print(Pizza.margherita())      
print(Pizza.hawaiian())
mine = Pizza(12,["Mozzerella", "Marinara", "Pepperoni"])
print(Pizza.circle_area(4))
print(mine.area())
print(Pizza.made())
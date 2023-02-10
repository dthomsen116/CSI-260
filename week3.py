"""
Lab: Gives a chance to practice implementing a class in Python.

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


class Country:
    """Create class Country."""

    area = 0
    population = 0
    name = "Country"

    def __init__(self, name, population, area):
        """Create initialization function."""
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        """Create function to determine the lager of two countries."""
        if self.area > other.area:
            return (True)
            # print(self.name + " is the larger country" + '\n' )
        elif self.area <= other.area:
            return (False)
            # print(self.name + " is the smaller country" + '\n' )

    def population_density(self):
        """Calculate the population density (pop/area) and format output."""
        popdens = (self.population / self.area)
        return (float(f'{popdens:.4f}'))

    def summary(self):
        """Summarize the country and state all previous information."""
        return (self.name + " has a population of "
                + str(self.population)
                + " people and is "
                + str(self.area)
                + " square km. It therefore has a population density of "
                + format(self.population_density(), '.4f')
                + " people per square km.")


# KingdomOfAwesome = Country("Kingdom of Awesome", 10, 2)
# Uraguay = Country("Uraguay", 999, 10109)
# MakeBelieve = Country("MakeBelieve", 1000, 10000)

# print(Uraguay.name)
# print(Uraguay.population)
# print(Uraguay.area)

# Uraguay.is_larger(MakeBelieve)
# print(Uraguay.population_density())
# print(KingdomOfAwesome.summary())
# Uraguay.summary()

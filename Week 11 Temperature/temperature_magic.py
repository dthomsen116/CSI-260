"""
Author: David Thomsen
Class: CSI-260-01
Assignment: Week 11 Lab
Due Date: April 11, 2023
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

"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius"""
        self.celsius = degrees

    def __str__(self):
        """Return a representation of the temperature."""
        return f"{self.celsius}°C"

    def __repr__(self):
        """Return a string representation of the temperature."""
        return f"Temperature({self.celsius})"

    @property
    def fahrenheit(self):
        """Return the temperature in degrees fahrenheit."""
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, degrees):
        """Set the temperature in degrees fahrenheit.
        """
        self.celsius = (degrees - 32) / 1.8

    @property
    def kelvin(self):
        """Return the temperature in degrees kelvin."""
        return self.celsius + 273.15
 
    @kelvin.setter
    def kelvin(self, degrees):
        """Set the temperature in degrees kelvin.
        """
        self.celsius = degrees - 273.15
    

    def __eq__(self, other):
        """Return True if the temperatures are equal."""
        
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        else: 
            other = Temperature(other)
            return self.celsius == other.celsius

    def __lt__(self, other):
        """Return True if this temperature is less than the other."""
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        else: 
            other = Temperature(other)
            return self.celsius < other.celsius

    def __le__(self, other):
        """Return True if this temperature is less than or equal to the other."""
        if isinstance(other, Temperature):
            return self.celsius <= other.celsius
        else: 
            other = Temperature(other)
            return self.celsius <= other.celsius

    def __gt__(self, other):
        """Return True if this temperature greater less than the other."""
        if isinstance(other, Temperature):
            return self.celsius > other.celsius
        else: 
            other = Temperature(other)
            return self.celsius > other.celsius

    def __ge__(self, other):
        """Return True if this temperature is greater than or equal to the other."""
        if isinstance(other, Temperature):
            return self.celsius >= other.celsius
        else: 
            other = Temperature(other)
            return self.celsius >=  other.celsius
        
    def __add__(self, other):
        """Return the sum of this temperature and the other."""
        if isinstance(other, Temperature):
            return Temperature(self.celsius + other.celsius)
        else: 
            other = Temperature(other)
            return Temperature(self.celsius + other.celsius)
        
    def __radd__(self, other):
        """Add a temperature to an object that does not have an __add__ method."""
        if not isinstance(other, Temperature):
            other = Temperature(other)
        return Temperature(other.celsius + self.celsius)
    
    def __iadd__(self, other):
        """Add a temperature to an object that does not have an __add__ method."""
        if not isinstance(other, Temperature):
            other = Temperature(other)
        self.celsius += other.celsius
        return(self)

    def __sub__(self, other):
        """Return the difference between this temperature and the other."""
        if isinstance(other, Temperature):
            return Temperature(self.celsius - other.celsius)
        else: 
            other = Temperature(other)
            return Temperature(self.celsius - other.celsius)
        
    def __rsub__(self, other):
        """Add a temperature to an object that does not have an __add__ method."""
        if not isinstance(other, Temperature):
            other = Temperature(other)
        return Temperature(other.celsius - self.celsius)
    
    def __isub__(self, other):
        """Add a temperature to an object that does not have an __add__ method."""
        if not isinstance(other, Temperature):
            other = Temperature(other)
        self.celsius -= other.celsius
        return(self)
    
    def __hash__ (self):
        return(hash(str(self)))
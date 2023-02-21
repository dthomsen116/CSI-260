"""
define classes Car, Truck and Motorcycle in this file 
They should extend the Vehicle base class 
"""
<<<<<<< HEAD
from vehiclebook import Vehicle
=======
from vehicle import Vehicle
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765

class Car(Vehicle):
  wheels = 4
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super() .__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s
<<<<<<< HEAD

=======
  
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765
class Truck(Vehicle):
  wheels = 18
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super() .__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s
<<<<<<< HEAD

=======
  
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765
class Motorcycle(Vehicle):
  wheels = 2
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super() .__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s

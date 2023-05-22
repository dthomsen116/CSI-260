class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.
    Attributes:
        wheels: An integer representing the number of   wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    base_sale_price = 2000
    wheels = 0
    _vehicles = []

    def __init__(self, miles, make, model, year):
        """initilizes the function
        """
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self._vehicles.append(self)

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is not None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        s = "This car is a " + str(self.make) + " " + str(self.model)
        return s

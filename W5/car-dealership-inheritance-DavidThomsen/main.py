<<<<<<< HEAD
<<<<<<< HEAD
from vehicle_types import Car, Truck, Motorcycle
import sys
from vehiclebook import Vehicle


class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.garage = []
        self.choices = {
            "1": self.show_vehicles,
            "2": self.add_Car,
            "3": self.add_Truck,
            "4": self.add_Motorcycle,
            "5": self.quit,
        }

    def display_menu(self):
        print("""\
Vehicle Menu

1. Show all vehicles
2. add car
3. add truck
4. add motorcycle
5. Quit
""")

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_vehicles(self):
        for i in self.garage:
          print(i)

    def add_Car(self):
        self.garage.append(
            Car(
                int(input("How many miles on the vehicle?: ")),
                input("What is the make of the vehicle?: "),
                input("What is the model of the vehicle?: "),
                int(input("What is the year of the vehicle?: ")),
                int(input("What is the fuel capacity?: "))
            ))

    def add_Truck(self):
        self.garage.append(
            Truck(
                int(input("How many miles on the vehicle?: ")),
                input("What is the make of the vehicle?: "),
                input("What is the model of the vehicle?: "),
                int(input("What is the year of the vehicle?: ")),
                int(input("What is the fuel capacity?: "))
            ))

    def add_Motorcycle(self):
        self.garage.append(
            Motorcycle(
                int(input("How many miles on the vehicle?: ")),
                input("What is the make of the vehicle?: "),
                input("What is the model of the vehicle?: "),
                int(input("What is the year of the vehicle?: ")),
                int(input("What is the fuel capacity?: "))
            ))

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
=======
=======
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765
from vehicle_types import Car, Motorcycle, Truck

A=Car(10000,"Honda", "CRV", 2020,35)
print (A.miles)
print(A.purchase_price())
print(A.sale_price())
print(A)

B = Truck(10000,"MAC", "Truck", 2020, 20)
print (B.miles)
print(B.purchase_price())
print(B.sale_price())
print(B)

C = Motorcycle(10000,"Harley Davidson", "Chopper", 2020, 20)
print (C.miles)
print(C.purchase_price())
print(C.sale_price())
<<<<<<< HEAD
print(C)
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765
=======
print(C)
>>>>>>> 2ea9319b822c48bd290ece2dbdc9142520b0d765

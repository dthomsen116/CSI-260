import sys
from medical import Patient,Procedure


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.inventory = []
        self.choices = {
            "1": self.get_patient,
            "2": self.add_patient,
            "3": self.delete_patient,
            "4": self.save_patients,
            "5": self.load_patients,
            "6": self.quit,
        }

    def display_menu(self):
        print("""\
Notebook Menu

1. Get patient
2. Add patient
3. Delete patient
4. Save patients
5. Load patient
6. Quit
"""
        )

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

    def get_patient(self):
        inputid = int(input("provide the patient's ID: "))
        for i in Patient.__all_patients:
            if inputid == Patient.id:
                return(self)
            else:
                None
    
    def add_patient(self):
        Patient.__all_patients.append(
            Patient(
                input("First Name?: "),
                input("Last Name?: "),
                input("Address?: "),
                input("Phone?: "),
                input("Emergency Contact?: "),
                input("Emergency Number?: ")
                ))
    
    def delete_patient(self):
        pass
                
    # def save_patients(self):
    #     pass
        
    # def load_patients(self):
    #     pass

        
        

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()


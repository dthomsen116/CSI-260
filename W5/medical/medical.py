"""
Lab: Week 4 Lab – Patients and Procedures

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
import pickle

class Patient:
    """Create class Patient."""
    __nextId = 0
    __all_patients = {}    

    def __init__(self, firstname, lastname, address, phone, emerCon, emerNum):
        """Create initialization function."""
        self.firstname = firstname
        self.lastname = lastname    
        self.address = address
        self.phone = phone
        self.emerCon = emerCon
        self.emerNum = emerNum

        self.__class__.__nextId += 1
        self.id = __class__.__nextId
        
        @classmethod
        def get_patient(id):
            if id in __class__.__all_patients:
                return __class__.__all_patients

        @classmethod
        def delete_patient(id):
            if id in __class__.__all_patients:        
                __class__.__all_patients.pop(id)

        @classmethod
        def save_patient():
            pickle.dump(__class__.__all_patients, open("patient.txt", "wb"))

        @classmethod
        def load_patient():
            pickle.load(__class__.__all_patients, open("patient.txt", "rb"))
            __class__.__nextId = max(__class__.__all_patients) + 1
        
        def add_proc(self, newproc):
            self.myproc.append(newproc)
            
        def remove_proc(self, oldproc):
            self.myproc.pop(oldproc)
        

    def __str__(self):
        return ("Name: " + str(self.firstname) + " " + str(self.lastname) + '\n' +
                "Address: " + str(self.address) + '\n' +
                "Phone: " + str(self.phone) + '\n' +
                "Emergency Contact: " + str(self.emerCon) + '\n' +
                "Emergency Num: " + str(self.emerNum) + '\n'
                    )
         

class Procedure:
    """Create class Procedure."""
    __nextProId = 0   

    def __init__(self, firstname, lastname, date, doctor, cost):
        """Create initialization function."""
        self.firstname = firstname
        self.lastname = lastname
        self.date = date
        self.doctor = doctor
        self.cost = cost
        
        self.__class__.__nextProId += 1
        self.id = __class__.__nextProId
        
    def __str__(self):
        return ("Name: " + str(self.firstname) + " " + str(self.lastname) + '\n' +
               "Date: " + str(self.date) + '\n' +
               "Doctor: " + str(self.doctor) + '\n' +
               "Cost: " + str(self.cost) + '\n' +
               "ProcedureID: " + str(self.id) + '\n'
                )



    
Abijah = Patient('Abijah', 'Buttendorf', 'The Boonies', '999-999-9999', 'Matt', '111-111-1111')
AbijahPro = Procedure("Abijah", "Buttendorf", "12/12/12", "Dr. Gleason", "2500")

# print(Abijah)
# print(AbijahPro)

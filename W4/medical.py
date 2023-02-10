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
        self.__id = __class__.__nextId
        
        __class__.__all_patients[self.__id] = self
        
        """adds one to the ID number and gives it to the patient."""


    def __str__():
        pass
    
    def get_patient():
        pass
    
    def delete_patient():
        pass
    
    def save_patients():
        pass
    
    def load_patients():
        pass
    
Abijah = Patient('Abijah', 'Buttendorf', 'The Boonies', '999-999-9999', 'Matt', '111-111-1111')

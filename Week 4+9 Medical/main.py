"""
Lab: Week 4 Lab – Patients and Procedures

Author: David Thomsen and Sean Sawyers-Abbott
Class: CSI-260
Assignment: Week 4 Lab
Due Date: February 27, 2023

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
from medical import Patient

Patient.load_patients()

mainMenu = """
Medical Menu

1. Get Patient
2. Add Patient
3. Exit
"""

patientMenu = """
Patient Menu

1. Modify Patient
2. Delete Patient
3. Add Procedure
4. Exit
"""

mainExit = False
while not mainExit:
  
  print (mainMenu)
  
  choice = input("Choose an option: ")
  if choice.isnumeric():
    choice = int(choice)
    
  match (choice):
    case 1:
      pat = Patient.get_patient()
      if (pat is not None):
        patExit = False

        while (patExit == False):
          print(pat.__str__())
          print(patientMenu)
          
          patChoice = input("Choose an option: ")
          if patChoice.isnumeric():
            patChoice = int(patChoice)
            
          match (patChoice):
            case 1:
              pat.modify_patient()
              patExit = True
            case 2:
              Patient.delete_patient(pat.id)
              patExit = True
            case 3:
              pat.add_procedure()
              patExit = True
            case 4:
              patExit = True
            case other:
              print("\nPlease input a value 1-4")
      else:
        print("\nPatient does not exist")
    case 2:
      Patient.add_patient()
    case 3:
      mainExit = True
      Patient.save_patients()
    case other:
      print("\nPlease input a value 1-3")
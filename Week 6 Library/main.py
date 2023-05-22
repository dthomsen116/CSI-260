"""Library Catalog

Author: David Thomsen and Sean Sawyers-Abbott 
Class: CSI-260-01
Assignment: Library Project
Due Date: 03/12/2023

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
from catalog import Catalog

menu = """
Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add item to catalog
4. Remove item from catalog
5. Exit"""

myLib = Catalog()

exit = False

while not exit:
  print(menu)
  choice = input("\nChoose an option: ")
  if choice.isnumeric():
    choice = int(choice)
  match choice:
    case 1:
      pass
    case 2:
      myLib.__str__()
    case 3:
      myLib.add()
    case 4:
      myLib.remove()
    case 5:
      myLib.save()
      exit = True
    case other:
      print("\nPlease input a value 1-5")
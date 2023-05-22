from library import LibraryItem, Book, DVD, Magazine
from categorytags import CategoryTags
import pickle

class Catalog:
  """ Catalog to store the LibraryItems
  """
  
  name = "CSI LIbrary"
  __items__ = []
  
  def __init__(self):
    """ Initialize a Catalog
    """
    
    self.load()
    print(f"{self.name} created")

  def __str__(self):
    """ Prints every item in the catalog
    """

    print("\n******** CATALOG LIST ********")
    for item in range(len(Catalog.__items__)):
      print(f"\n{item + 1}:")
      Catalog.__items__[item].__str__()
    print("\n******************************")
    print()

  def save(self):
    """ Saves all items to a file catalog.pickle
    """
    
    pickle.dump(Catalog.__items__, open("catalog.pickle", "wb"))
    
  def load(self):
    """ Loads the catalog.pickle file
    """
    
    try: # checks if the file exists
        file = open("catalog.pickle", "rb")
    except IOError: # if the file does not exist
        data = [] # creates an empty list
        file = open("catalog.pickle", 'wb') # creates the file
        pickle.dump(data, file) # dumps the empty dict into the file
        file.close() # closes the file
    else:
        try: # checks if the file is empty
          data = pickle.load(file)
        except EOFError:
          data = [] # creates an empty dict
          file = open("patient.pickle", 'wb') # creates the file
          pickle.dump(data, file) # dumps the empty dict into the file
        file.close() # closes the file
      
    Catalog.__items__ = data
    
  def add(self):
    """ Add an item to the catalog
    """

    found = False
    item = None
    
    while not found:
      type = input("\nWhat type of item are you adding (Book = 1, DVD = 2, Magazine = 3, Exit = 4): ")
      if type.isnumeric():
        type = int(type)
      match type:
        case 1:
          item = self.addBook()
          found = True
        case 2:
          item = self.addDVD()
          found = True
        case 3:
          item = self.addMagazine()
          found = True
        case 4:
          found = True
        case other:
          print("\nPlease input a value 1-5")
    if item is not None:
      Catalog.__items__.append(item)

  def remove(self):
    """ Removes an item from the Catalog
    """

    size = len(Catalog.__items__)

    if size > 0:
      findNum = False
      itemNum = 0
      
      self.__str__()
      while not findNum:
        itemNum = input("Input the item number to remove (0 to Exit): ")
        if itemNum.isnumeric():
          itemNum = int(itemNum)
        else:
          print(f"Please input a value 0-{size}")
        if itemNum < 0 or itemNum > size:
          print(f"Please input a value 0-{size}")
        else:
          findNum = True
      if itemNum > 0:
        Catalog.__items__.pop(itemNum - 1)
    else:
      print("\nThere are no items")
    
  def addBook(self):
    """ Creates a Book item to be added to the Catalog
    """
    
    return Book(
      input("Name: "),
      int(input("Call Number: ")),
      input("Author(s): "),
      input("Description: "),
      input("Publisher: "),
      int(input("Year Published: "))
    )

  def addDVD(self):
    """ Creates a DVD item to be added to the Catalog
    """
    
    return DVD(
      input("Name: "),
      int(input("Call Number: ")),
      input("Description: "),
      input("Producer: "),
      int(input("Year: "))
    )

  def addMagazine(self):
    """ Creates a Magazine item to be added to the Catalog
    """
    
    return Magazine(
      input("Name: "),
      int(input("Call Number: ")),
      input("Description: "),
      input("Publisher: "),
      int(input("Year: "))
    )
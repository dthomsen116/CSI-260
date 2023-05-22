from abc import ABC, abstractmethod

class LibraryItem(ABC):
  """ Base class for all items stored in a library catalog

  Provides a simple LibraryItem with only a few attributes
  """
  
  def __init__(self, name, callNumber, tags = None):
    """ Initialize a LibraryItem

    :param name: (string) Name of item
    :param callNumber: (string) Local identifying number for the item
    :param tags: (list) List of CategoryTags
    """

    super().__init__()
    self.name = name
    self.callNumber = callNumber
    if tags:
        self.tags = tags
    else:
        self.tags = list()

  @abstractmethod
  def __str__(self):
    """ Print the information of a LibraryItem
    """

    print(self.__class__.__name__)
    print(f"Call Number: {self.callNumber}")
    print(f"Title: {self.name}")
    
class Book(LibraryItem):
  """ Subclass of LibraryItem for physical books
  """
  
  def __init__(self, name, callNumber, authors, description, publisher, year, tags = None):
    """ Initializes a Book

    :param name: (string) Name of book
    :param callNumber: (string) Local identifying number for the book
    :param authors: (string) Authors of the book
    :param description: (string) Description of the book
    :param publisher: (string) Publisher of the book
    :param year: (int) Year the book was published
    :param tags: (list) List of CategoryTags
    """

    super().__init__(name, callNumber, tags)
    self.authors = authors
    self.description = description
    self.publisher = publisher
    self.year = year

  def __str__(self):
    """ Prints the information of the Book
    """
    super().__str__()
    print(f"Authors: {self.authors}")
    
class DVD(LibraryItem):
  """ Subclass of LibraryItem for physical DVD's
  """
  
  def __init__(self, name, callNumber, description, producers, year, tags = None):
    """ Initializes a DVD

    :param name: (string) Name of DVD
    :param callNumber: (string) Local identifying number for the DVD
    :param description: (string) Description of the DVD
    :param producers: (string) Producers of the DVD
    :param year: (int) Year the DVD was published
    :param tags: (list) List of CategoryTags
    """

    super().__init__(name, callNumber, tags)
    self.description = description
    self.producers = producers
    self.year = year

  def __str__(self):
    """ Prints the information of the DVD
    """
    
    super().__str__()
    print(f"Producer: {self.producer}")

class Magazine(LibraryItem):
  """ Subclass of LibraryItem for physical Magazines
  """
  
  def __init__(self, name, callNumber, description, publisher, year, tags = None):
    """ Initializes a Magazine

    :param name: (string) Name of Magazine
    :param callNumber: (string) Local identifying number for the Magazine
    :param description: (string) Description of the Magazine
    :param publisher: (string) Publisher of the Magazine
    :param year: (int) Year the Magazine was published
    :param tags: (list) List of CategoryTags
    """

    super().__init__(name, callNumber, tags)
    self.description = description
    self.publisher = publisher
    self.year = year

  def __str__(self):
    """ Prints the information of the Magazine
    """
    
    super().__str__()
    print(f"Publisher: {self.publisher}")
import pickle

class Procedure:
  """ Class to hold information about a Patient's Procedure
  """
  
  _nextProId = 0

  def __init__(self, name, date, doctor, cost):
    """ Initializes a Procedure instance

    :param name: (string) Name of the Procedure
    :param date: (string) Date of the Procedure
    :param doctor: (string) Name of the doctor assigned to the Procedure
    :param cost: (float) Cost of the Procedure
    """

    self.name = name
    self.date = date
    self.doctor = doctor
    self.cost = cost

    Procedure._nextProId += 1
    self.id = Procedure._nextProId

  def __str__(self):
    """ Creates a string of the Procedure's information

    :returns: (string) Procedure's information
    """
    
    return (f"Name: {self.name}\nDate: {self.date}\nDoctor: {self.doctor}\nCost: {self.cost}\nProcedureID: {self.id}\n")

class Patient:
  """ Class to hold information about a Patient
  """
  
  _nextId = 0
  _all_patients = {}

  def __init__(self, firstname, lastname, address, phone, emerCon, emerNum):
    """ Initializes a Patient instance
      
    :param firstname: (string) First name of the patient
    :param lastname: (string) Last name of the patient
    :param address: (string) Address of the patient
    :param phone: (string) Phone number of the patient
    :param emerCon: (string) Name of the patient's emergency contact
    :param emerNum: (string) Phone number of the patient's emergency contact
    """
    
    self.firstname = firstname
    self.lastname = lastname
    self.address = address
    self.phone = phone
    self.emerCon = emerCon
    self.emerNum = emerNum
    self.procedures = []
    
    Patient._nextId += 1
    self.id = Patient._nextId

  @classmethod
  def get_patient(cls):
    """ Gets a patient
    
    :returns: Patient if id found, None if not
    """
    
    id = input("\nInput ID: ")
    if (id.isnumeric()):
      id = int(id)
    
    if id in Patient._all_patients:
      return Patient._all_patients[id]
    return None

  @classmethod
  def delete_patient(cls, id):
    """ Deletes a patient
    """
    
    Patient._nextId -= 1
    
    if (id in Patient._all_patients):
      Patient._all_patients.pop(id)
      print(f"\nPatient {id} deleted")

  @classmethod
  def save_patients(cls):
    """ Saves all_patients to a file patient.pickle
    """
    
    pickle.dump(Patient._all_patients, open("patient.pickle", "wb"))

  @classmethod
  def load_patients(cls):
    """ Loads the patient.pickle and sets the nextId to the correct value
    """

    try: # checks if the file exists
        file = open("patient.pickle", "rb")
    except IOError: # if the file does not exist
        data = {} # creates an empty dict
        file = open("patient.pickle", 'wb') # creates the file
        pickle.dump(data, file) # dumps the empty dict into the file
        file.close() # closes the file
    else:
        try: # checks if the file is empty
          data = pickle.load(file)
        except EOFError:
          data = {} # creates an empty dict
          file = open("patient.pickle", 'wb') # creates the file
          pickle.dump(data, file) # dumps the empty dict into the file
        file.close() # closes the file
      
    Patient._all_patients = data
    Patient._nextId = len(Patient._all_patients)

  @classmethod
  def add_patient(cls):
    """ Adds a patient to all_patients
    """
    
    newPatient = Patient(input("\nFirst Name?: "),
                         input("Last Name?: "),
                         input("Address?: "),
                         input("Phone?: "),
                         input("Emergency Contact?: "),
                         input("Emergency Number?: "))
    Patient._all_patients[newPatient.id] = newPatient
    print(f"\nPatient {newPatient.firstname} {newPatient.lastname} created with ID {newPatient.id}")

  def modify_patient(self):
    """ Modifies a Patient's information
    """

    data = input("Please enter the new data: ")
    
    modExit = False
    while (modExit == False):
      print("\nModify Menu\n\n1. First Name\n2. Last Name\n3. Address\n4. Phone Number\n5. Emergency Contact\n6. Emergency Phone Number\n7. Exit\n")

      modChoice = input("Choose an option: ")
      if (modChoice.isnumeric()):
        modChoice = int(modChoice)
      match (modChoice):
        case 1:
          self.firstname = data
          modExit = True
        case 2:
          self.lastname = data
          modExit = True
        case 3:
          self.address = data
          modExit = True
        case 4:
          self.phone = data
          modExit = True
        case 5:
          self.emerCon = data
          modExit = True
        case 6:
          self.emerNum = data
          modExit = True
        case 7:
          modExit = True
        case other:
          print("Please input a value 1-7")

  def add_procedure(self):
    """ Adds a Procedure
    """
    
    self.procedures.append(Procedure(input("\nProcedure Name: "),
                                     input("Date: "), 
                                     input("Doctor: "), 
                                     input("Cost: ")))

  def __str__(self):
    """ Creates a string of the Patient's information

    :returns: (string) Patient's information
    """
    
    returnString = f"\nName: {self.firstname} {self.lastname}\nAddress: {self.address}\nPhone: {self.phone}\nEmergency Contact: {self.emerCon}\nEmergency Phone: {self.emerNum}\n\nProcedures:"
    if self.procedures:
      for procedure in self.procedures:
        returnString += '\n' + procedure.__str__()
    else:
      returnString += "\nNone"
    return (returnString)
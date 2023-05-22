In this week's lab, you will be making an application for a hospital to manage patients and medical procedures.  For the purpose of this lab, we will be ignoring some important considerations for such an application: we will not worry about data privacy or collecting a patient's past medical history.

The relevant information that needs to be stored for a patient is their first name, last name, address,  phone number, and finally the name and phone number of an emergency contact.  Additionally, each patient should be assigned a unique ID number, and will also need to keep track of the procedures that they have scheduled.

For procedures, we need to know the name of the procedure, the date it is scheduled for, the name of the medical practitioner performing the procedure, and the procedure's cost.  Like patients, each procedure should be assigned a unique ID number.

 
Part 1
You must define two classes: Patient and Procedure for maintaining this information inside of a file called medical.py. 

Patient needs to have an initializer, which takes as arguments all of the information relevant to a patient, except the ID number and procedures, and sets instance variables (attributes) appropriately.  The next available ID number must be stored as a "private" class variable, and when a new Patient is initialized they must be assigned this ID number, and the next available ID number must be incremented.  On initialization a patient will not have any procedures scheduled.

The Patient class must also have a class variable _all_patients: a dictionary mapping id numbers to Patient instances (leading underscore because this will be a "private" variable), and on initialization each patient must be added to this dictionary.

Procedure also needs to have an initializer, which takes as arguments all of the information relevant to a procedure, except the ID number, and sets instance variables (attributes) appropriately.  Like with Patient, the next available ID number for procedures must be stored as a "private" class variable, and when a new Procedure is initialized it must be assigned this ID number, and the next available ID number must be incremented.

On top of the above specification, Patient and Procedure should each have a method __str__ that returns a nicely formatted string representation of all the data about that instance.  The string returned by the __str__ method of Patient should contain a description of each of that patient's procedures.

Hint: how can Patient.__str__ use Procedure.__str__ (remember DRY).

Patient must also have a method add_procedure that adds a Procedure for that Patient.

Finally, Patient must also have four class methods:

get_patient, which takes the ID of a Patient and returns the Patient with that ID if it exists in _all_patients otherwise None
delete_patient, which takes the ID of a Patient and deletes that entry from _all_patients.  If the given ID does not exist in _all_patients then nothing should happen.
save_patients, which pickles the _all_patients dictionary and saves it to a file.
     if you are not familiar with pickle, see
     https://wiki.python.org/moin/UsingPickle Links to an external site. 
load_patients, which loads the pickled dictionary from a file, and then appropriately sets the next available ids for patients and procedures so that newly added patients will still get a unique id.
 
Part 2
In a separate file: week4.py, you will import these classes from medical.py and use them in a program with a command line interface.

The program must present the user with a repeating menu:

Look up a patient by ID number.
Add a new patient
Quit
On selecting (1), the user must be prompted for the patient's ID number.  If that is not the ID of an existing patient, the user should be told as much and returned to the main menu.  If it is the ID of an existing patient, that patients' information must be printed to screen, and the user is offered a new menu with the ability to (a) modify a patient's attributes, (b) delete a patient, or (c) add a procedure.  On selection of one of these options, the user must be prompted for the appropriate information, and returned to the original menu.


When the program quits it should call Patient.save_patients to save the patients to a file, and each time the program starts, it should try to load the pickled dictionary from the file (using Patient.load_patients). If the file does not exist, the program should start with an empty dictionary.

 
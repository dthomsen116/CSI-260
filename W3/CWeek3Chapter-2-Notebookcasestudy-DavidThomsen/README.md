The following assignment is based on the case study in Chapter 2.  A careful reading of the case study should provide answers to the problems.

Add the following functionality to the program:

For parts 1 & 2 we are going to reduce redundant code in the methods modify_memo and modify_tags to encapsulate the logic for finding a given note in the notebook.

 

1.  Create a new method _find_note(note_id).  

def _find_note(self, note_id):

    """Locate the note with the given id.

    param: note_id (int) the note_id to be found

    return: the note or None if not found

    """

2.  Modify the methods modify_tags and modify_memo to make use of the _find_note method:

3.  Fix two bugs that exist when modifying notes:

    a.  The notebook crashes when we enter a note ID that does not exist.

    b.  Even when we enter the correct ID, it will crash because the note IDs are integers but our menu is passing a string.

4.  When adding a new note, allow the user to enter the tags that apply for that note.

5. Modify notebook.py so:

Notes store an optional title. Your variable must be called "title" and must be stored as a string.  

You should update the following methods to reflect the change:

Note.__init__(self, memo, tags="", title="")

Note.match(self, filter_text)

Notebook.new_note(self, memo, tags="", title="")

You should add the following method:

Notebook.modify_title(self, note_id, title)

You will also need to modify the main.py
show_notes,search_notes,self.add_note and self.modify_note,
            



Solutions to 1-3 exist in the reading.
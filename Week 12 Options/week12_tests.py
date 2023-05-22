"""Tests for Week 11 Lab.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import unittest
from options import Options
import sys

# define constants used by tests

STUDENT_CODE = ["options.py"]


class TestWeek11(unittest.TestCase):
    """Main testing class for Week 11 Lab."""
    
    def test_01_initializer(self):
        """Test if initializer works as specified."""
        
        # positional
        options = Options("debug", "verbose")        
        message = "Option not initialized correctly from positional argument."
        
        self.assertEqual(options["debug"], True, message)
        self.assertEqual(options["verbose"], True, message)
        
        # positional type
        message = ("Must raise TypeError for any positional argument that is "
                   "not a string.")

        with self.assertRaises(TypeError, msg=message):
            options = Options(True)
        
        with self.assertRaises(TypeError, msg=message):
            options = Options(4.5)
            
        # keywords
        options = Options(log_file="logging.txt", port=80)
        message = "Option not initialized correctly from keyword argument."
        
        self.assertEqual(options["log_file"], "logging.txt", message)
        self.assertEqual(options["port"], 80, message)
        
        # combined
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        message = "Option not initialized using a combination of arguments."
        self.assertEqual(options["debug"], True, message)
        self.assertEqual(options["verbose"], True, message)
        self.assertEqual(options["log_file"], "logging.txt", message)
        self.assertEqual(options["port"], 80, message)
        
    def test_02_getitem(self):
        """Test if getting items with []s works as specified."""
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        message = "Retrieving an unspecfied option must return False."
        # no need to check specified options, since checked in previous test
        self.assertEqual(options["fsdgjhgd"], False, message)
    
    def test_03_getattr(self):
        """Test if getting items as attributesworks as specified."""
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        message = "Retrieving options as attributes not working correctly."
        try:
            self.assertEqual(options.debug, True, message)
            self.assertEqual(options.verbose, True, message)
            self.assertEqual(options.log_file, "logging.txt", message)
            self.assertEqual(options.port, 80, message)
            self.assertEqual(options["fsdgjhgd"], False, 
                             "Retrieving an unspecfied option must "
                             "return False.")
        except AttributeError:
            self.fail("Accessing an option as an attribute should not raise"
                      " an AttributeError.  Have you implemented __getattr__?")
        
    def test_04_setitem(self):
        """Test if setting items with []s works as specified."""
        options = Options()
        options["test"] = "test_value"
        message = ("It must be possible to set options with []s, e.g. "
                   'options["log_file"] = "new_logging.txt"')
        self.assertEqual(options["test"], "test_value", message)
        self.assertEqual(options.test, "test_value", message)

        message = ("Must raise TypeError when attempting to set an option "
                   "with a name that is not a string.")
                   
        with self.assertRaises(TypeError, msg=message):
            options = Options(True)
        
        with self.assertRaises(TypeError, msg=message):
            options = Options(4.5)

    def test_05_setattr(self):
        """Test if setting attributes works as specified."""
        options = Options()
        options.test = "test_value"
        message = ("It must be possible to set options with []s, e.g. "
                   'options["log_file"] = "new_logging.txt"')
        self.assertEqual(options["test"], "test_value", message)
        self.assertEqual(options.test, "test_value", message)
        
    def test_06_delattr(self):
        """Test if deleting options works as specified."""
        options = Options(test="test_value")
        del options["test"]
        self.assertEqual(options.test, False, 
                         "Deleting options by deleting dict keys not working "
                         "as specified.  You should not have needed to "
                         "override __delitem__")
        options["test"] = "test_value"
        del options.test
        self.assertEqual(options.test, False, 
                         "Deleting options by deleting attributes not working "
                         "as specified.  Did you implement __delattr__?")
    
    def test_07_style(self):
        """Run the linter and check that the header is there."""
        try:
            from flake8.api import legacy as flake8
            # noqa on the following since just importing to test installed
            import pep8ext_naming  # noqa
            import flake8_docstrings  # noqa
            print("\nLinting Code...\n" + "=" * 15)

            style_guide = flake8.get_style_guide()

            report = style_guide.check_files(STUDENT_CODE)

            self.assertEqual(report.total_errors, 0,
                             "You should fix all linting errors "
                             "before submission in order to receive full "
                             "credit!")

            for module in STUDENT_CODE:
                self.check_header(module)

            print("Passing linter tests!")

        except ImportError:
            print("""
### WARNING: Unable to import flake8 and/or extensions, so cannot \
properly lint your code. ###

Please install flake8, pep8-naming, and flake8-docstrings to auto-check \
whether you are adhering to proper style and docstring conventions.

To install, run:

pip install flake8 pep8-naming flake8-docstrings

""")

    def check_header(self, module):
        """Check the header of the given module."""
        docstring = sys.modules[module[:-3]].__doc__
        for check in ['Author:', 'Class:', 'Assignment:',
                      'Certification of Authenticity:']:
            self.assertIn(check, docstring,
                          "Missing '{}' in {}'s docstring".format(
                            check, module))


if __name__ == '__main__':
    unittest.main(failfast=True)

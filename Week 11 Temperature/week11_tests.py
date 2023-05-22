"""Tests for Week 11 Lab.

Written by Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import unittest
from temperature_magic import Temperature
import sys


# define constants used by tests

STUDENT_CODE = ["temperature_magic.py"]


class TestWeek10(unittest.TestCase):
    """Main testing class for Week 10 Lab."""

    def test_01_str(self):
        """Test if str conversion works as specified."""
        message = "String conversion not correct"
        self.assertEqual(str(Temperature(45)),"45°C", message)
        self.assertEqual(str(Temperature(20.5)),"20.5°C", message)
        self.assertEqual(str(Temperature(-11.1)),"-11.1°C", message)

    def test_02_repr(self):
        """Test if repr conversion works as specified."""
        message = "repr conversion not correct"
        self.assertEqual(repr(Temperature(45)),"Temperature(45)", message)
        self.assertEqual(repr(Temperature(20.5)),"Temperature(20.5)", message)
        self.assertEqual(repr(Temperature(-11.1)),"Temperature(-11.1)", message)

    def test_03_equality(self):
        """Test == and != comparisons."""
        temperature = Temperature(20.5)
        temperature2 = Temperature(13.1)
        temperature3 = Temperature(20.5)
        
        self.assertFalse(temperature == temperature2,
                         "== comparison not correct"
                         " when comparing two temperatures")
        self.assertTrue(temperature == temperature3,
                         "== comparison not correct"
                         " when comparing two temperatures")
        self.assertFalse(temperature == 11,
                         "== comparison not correct"
                         " when comparing temperature and number")
        self.assertTrue(temperature == 20.5,
                         "== comparison not correct"
                         " when comparing temperature and number")        

        self.assertTrue(temperature != temperature2,
                         "!= comparison not correct"
                         " when comparing two temperatures")
        self.assertFalse(temperature != temperature3,
                         "!= comparison not correct"
                         " when comparing two temperatures")
        self.assertTrue(temperature != 11,
                         "!= comparison not correct"
                         " when comparing temperature and number")
        self.assertFalse(temperature != 20.5,
                         "!= comparison not correct"
                         " when comparing temperature and number")           

    def test_04_strict_inequalities(self):
        """Test < and >."""
        temperature = Temperature(20.5)
        temperature2 = Temperature(13.1)
        self.assertFalse(temperature < temperature2,
                         "< comparison not correct"
                         " when comparing two temperatures")
        self.assertFalse(temperature < temperature,
                         "< comparison not correct"
                         " when comparing two temperatures")
        self.assertFalse(temperature > temperature,
                         "> comparison not correct"
                         " when comparing two temperatures")        
        self.assertTrue(temperature > temperature2,
                        "> comparison not correct"
                        " when comparing two temperatures")        
        self.assertTrue(temperature < 25,
                        "< comparison not correct"
                        " when comparing temperature and number") 
        self.assertFalse(temperature > 25,
                         "> comparison not correct"
                         " when comparing temperature and number")
        self.assertTrue(10 < temperature,
                        "< comparison not correct"
                        " when comparing temperature and number") 
        self.assertFalse(25 < temperature,
                         "> comparison not correct"
                         " when comparing temperature and number")

    def test_05_inequalities(self):
        """Test <= and >=."""
        temperature = Temperature(20.5)
        self.assertTrue(temperature >= 10,
                        ">= comparison not correct")
        self.assertFalse(temperature <= 10,
                         "<= comparison not correct")

        self.assertTrue(temperature <= 20.5,
                        "<= comparison not correct")

        self.assertTrue(10 <= temperature,
                        "<= comparison not correct")
 
        self.assertFalse(10 >= temperature,
                         ">= comparison not correct")
                         
        self.assertTrue(20.5 >= temperature,
                        ">= comparison not correct")

        self.assertTrue(temperature >= Temperature(4),
                        ">= comparison not correct")

    def test_06_addition(self):
        """Test +."""
        temperature = Temperature(20.5)
        self.assertEqual((5 + temperature).celsius, 25.5,
                         "+ not correct")
        self.assertEqual((temperature + 5).celsius, 25.5,
                         "+ not correct")                         
        self.assertEqual((temperature + temperature).celsius, 41,
                         "+ not correct")
                         
    def test_07_subtraction(self):
        """Test -."""
        temperature = Temperature(20.5)
        self.assertEqual((temperature - 5).celsius, 15.5,
                         "- not correct")
        self.assertEqual((5 - temperature).celsius, -15.5,
                         "- not correct")                         
        self.assertEqual((temperature - temperature).celsius, 0,
                         "- not correct")
                         
    def test_08_inplace_addition(self):
        """Test +=."""
        temperature = Temperature(20.5)
        backup = temperature
        temperature += 5
        self.assertEqual(temperature.celsius, 25.5,
                         "+= not correct")
        self.assertEqual(backup.celsius, 25.5,
                         "+= not correct")
        temperature += Temperature(5)
        self.assertEqual(temperature.celsius, 30.5,
                         "+= not correct")
        self.assertEqual(backup.celsius, 30.5,
                         "+= not correct")

    def test_09_inplace_subtraction(self):
        """Test +=."""
        temperature = Temperature(20.5)
        backup = temperature
        temperature -= 5
        self.assertEqual(temperature.celsius, 15.5,
                         "-= not correct")
        self.assertEqual(backup.celsius, 15.5,
                         "-= not correct")
        temperature -= Temperature(5)
        self.assertEqual(temperature.celsius, 10.5,
                         "-= not correct")
        self.assertEqual(backup.celsius, 10.5,
                         "-= not correct")

    def test_10_hash(self):
        """Test hash."""
        self.assertEqual(hash(Temperature(20.5)), hash(Temperature(20.5)),
                         "hash not correct")
        self.assertNotEqual(hash(Temperature(20.5)), hash(Temperature(10.5)),
                         "hash not correct")

    def test_11_style(self):
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

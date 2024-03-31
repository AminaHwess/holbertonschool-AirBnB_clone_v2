#!/usr/bin/python3
"""
Unit tests for HBNBCommand class
"""

import console
import pep8
import unittest

HBNBCommand = console.HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Class for testing HBNBCommand"""

    def test_pep8_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings) in console.py.")

    def test_pep8_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings) in tests/test_console.py.")

    def test_hbnbcommand_instance(self):
        """Test if HBNBCommand is an instance of console.HBNBCommand"""
        self.assertIsInstance(HBNBCommand(), console.HBNBCommand,
                              "HBNBCommand is not an instance of console.HBNBCommand")

    def test_hbnbcommand_methods(self):
        """Test if HBNBCommand contains required methods"""
        hbnb_command = HBNBCommand()
        self.assertTrue(hasattr(hbnb_command, 'do_quit'),
                        "HBNBCommand does not have method do_quit")
        self.assertTrue(hasattr(hbnb_command, 'do_create'),
                        "HBNBCommand does not have method do_create")
        self.assertTrue(hasattr(hbnb_command, 'do_show'),
                        "HBNBCommand does not have method do_show")
        self.assertTrue(hasattr(hbnb_command, 'do_destroy'),
                        "HBNBCommand does not have method do_destroy")
        self.assertTrue(hasattr(hbnb_command, 'do_all'),
                        "HBNBCommand does not have method do_all")
        self.assertTrue(hasattr(hbnb_command, 'do_update'),
                        "HBNBCommand does not have method do_update")

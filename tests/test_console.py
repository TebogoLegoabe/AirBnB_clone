#!/usr/bin/python3
"""Unittests for the console"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestConsole(unittest.TestCase):

    def setUp(self):
        storage.reload()

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertEqual(f.getvalue(), 'Documented commands (type help <topic>):\n\nEOF  help  quit\n')

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            self.assertEqual(f.getvalue(), 'Quit command to exit the program\n')

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertEqual(f.getvalue(), '** id ** 1\n')

    def test_show_user(self):
        user = User(id=1, email='test@test.com', password='test')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User 1')
            self.assertEqual(f.getvalue(), str(user))

    def test_destroy_user(self):
        user = User(id=1, email='test@test.com', password='test')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User 1')
            self.assertEqual(f.getvalue(), '')

    def test_all_users(self):
        user1 = User(id=1, email='test1@test.com', password='test1')
        user2 = User(id=2, email='test2@test.com', password='test2')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            self.assertEqual(f.getvalue(), str(user1) + '\n' + str(user2))

    def test_press_enter(self):
    """When press enter no action has to been executed"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("\n")
    self.assertEqual(f.getvalue(), '')
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("            \n")
    self.assertEqual(f.getvalue(), '')

def test_wrong_command(self):
    """When press random words no action has to been executed"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("daasdas")
    self.assertEqual(f.getvalue(), '*** Unknown syntax: daasdas\n')

def test_help_with_args(self):
    """Test if all docstring were written"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("help quit")
    self.assertEqual(f.getvalue(), 'Quit command to exit the program\n\n')

def test_command_with_spaces(self):
    """Despite spaces the command has to be executed"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("     help        quit")
    self.assertEqual(f.getvalue(), 'Quit command to exit the program\n\n')

def test_quit(self):
    """Test quit"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("quit")
    self.assertEqual(f.getvalue(), '')

def test_EOF(self):
    """Test EOF"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("EOF")
    self.assertEqual(f.getvalue(), '\n')
if __name__ == "__main__":
    unittest.main()

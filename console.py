#!/usr/bin/python3
"""
This module contains the console (command interpreter) for
the Holberton School AirBnB project
"""
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This class contains the console for HBnB project"""

    prompt = '(hbnb)'

    def do_show(self, arg):
        """Prints str representation of an instance"""
        new_list = arg.split(" ")
        if len(new_list) == 0:
            print("** class name missing **")
        elif new_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(new_list) == 1:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            new_str = str(new_list[0] + '.' + new_list[1])
            for k, v in my_dict.items():
                if k == new_str:
                    print(v)
                    return
            print("** no instance found **")

    def help_show(self):
        """Help for show"""
        print("Prints the string representation of an instance.")

    def do_create(self, arg):
        """Creates new BaseModel objects"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def help_create(self):
        """Help for create"""
        print("Creates new instance of BaseModel, saves it, and prints the id")

    def do_quit(self, arg):
        """Execute quit"""
        sys.exit(1)

    def help_quit(self):
        """Help for quit"""
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """Execute EOF"""
        return True

    def help_EOF(self):
        """Help for EOF"""
        print("EOF command to exit the program")

    def emptyline(self):
        pass


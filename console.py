#!/usr/bin/python3
"""
This module contains the console (command interpreter) for
the Holberton School AirBnB project
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This class contains the console for HBnB project"""
    
    def __init__(self):
        """Constructor for console"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

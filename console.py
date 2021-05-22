#!/usr/bin/python3
"""
This module contains the console (command interpreter) for
the Holberton School AirBnB project
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd
import sys
import models
import json


class HBNBCommand(cmd.Cmd):
    """This class contains the console for HBnB project"""

    obj_dict = {"BaseModel": BaseModel(), "User": User()}
    prompt = '(hbnb)'

    def do_all(self, arg):
        """Prints all str representations of all instances based on class name
           if no class name, prints all instances of all objects"""
        arg_list = arg.split(" ")
        my_dict = models.storage.all()
        if len(arg) == 0:
            for i in my_dict.values():
                print(i)
        elif arg_list[0] not in self.obj_dict.keys():
            print("** class doesn't exist **")
        else:
            for k, v in my_dict.items():
                class_name = k.split('.')
                if class_name[0] == arg_list[0]:
                    print(v)

    def help_all(self):
        """Help for all"""
        print("Prints string representation of all instances")

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        arg_list = arg.split(" ")
        my_dict = models.storage.all()
        signal = 0
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.obj_dict.keys():
            print("** class doesn't exist **")
            return
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = str(arg_list[0] + '.' + arg_list[1])
            for k in my_dict.keys():
                if new_str == k:
                    signal = 1
                    break
            if signal == 0:
                print("** no instance found **")
                return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        elif len(arg_list) < 4:
            print("** value missing **")
            return
        else:
            new_dict = my_dict[new_str]
            try:
                attr = getattr(new_dict, arg_list[2])
                if type(attr) is int:
                    setattr(new_dict, arg_list[2], int(arg_list[3]))
                elif type(attr) is float:
                    setattr(new_dict, arg_list[2], float(arg_list[3]))
                else:
                    setattr(new_dict, arg_list[2], arg_list[3][1:-1])
            except:
                setattr(new_dict, arg_list[2], arg_list[3][1:-1])
        self.obj_dict[arg_list[0]].save()

    def do_show(self, arg):
        """Prints str representation of an instance"""
        new_list = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif new_list[0] not in self.obj_dict.keys():
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
        elif arg not in self.obj_dict.keys():
            print("** class doesn't exist **")
        else:
            obj = self.obj_dict[arg]
            obj.save()
            print(obj.id)

    def help_create(self):
        """Help for create"""
        print("Creates new instance of BaseModel, saves it, and prints the id")

    def do_destroy(self, arg):
        """Destroys an instance based on class name and id"""
        new_list = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif new_list[0] not in self.obj_dict.keys():
            print("** class doesn't exist **")
        elif len(new_list) == 1:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            new_str = str(new_list[0] + '.' + new_list[1])
            for k in my_dict.keys():
                if k == new_str:
                    my_dict.pop(k)
                    models.storage.save()
                    return
            print("** no instance found **")

    def help_destroy(self):
        """Help for destroy"""
        print("Destroys an instance of an object based on class name and id")

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

#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which serves as the command
interpreter for the AirBnB console.
"""

import sys
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine

current_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command interpreter for the AirBnB console.

    Attributes:
        prompt (str): The command prompt displayed to the user.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit the command interpreter and exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Quit the command interpreter and exit the program.

        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class with given parameters.

        Usage: create <Class name> <key1=value1> <key2=value2> ...
        """
        try:
            if not arg:
                raise SyntaxError("** class name missing **")

            class_name, *attributes = arg.split()
            if not class_name:
                raise SyntaxError("** class name missing **")

            kwargs = {}
            for attribute in attributes:
                match = re.match(r'(\w+)=(\S+)', attribute)
                if match:
                    key, value = match.groups()
                    # Handle escaped double quotes
                    if value.startswith('"') and value.endswith('"'):
                        value = (
                            value[1:-1]
                            .replace('_', ' ')
                            .replace('\\"', '"')
                        )
                    else:
                        try:
                            value = eval(value)
                        except (SyntaxError, NameError):
                            continue
                    kwargs[key] = value

            if kwargs == {}:
                obj = current_classes[class_name]()
            else:
                obj = current_classes[class_name](**kwargs)
                storage.new(obj)

            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in current_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if obj_key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[obj_key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name not in current_classes:
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_key = "{}.{}".format(class_name, args[1])
                    all_objs = storage.all()
                    if obj_key not in all_objs:
                        print("** no instance found **")
                    else:
                        del all_objs[obj_key]
                        storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print all string representations of instances.

        Usage: all [<class_name>]
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
        elif args[0] not in current_classes:
            print("** class doesn't exist **")
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args or args[0] not in current_classes:
            print(
                "** class name missing **" if not args
                else "** class doesn't exist **"
            )
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])

        if obj_key not in instance_objs:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = instance_objs[obj_key]
            attribute_name = args[2]
            attribute_value = ' '.join(args[3:]).strip('"')

            if hasattr(instance, attribute_name):
                attr_type = type(getattr(instance, attribute_name))
                setattr(instance, attribute_name, attr_type(attribute_value))
                storage.save()
            else:
                # Add the attribute if it doesn't exist
                setattr(instance, attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    # Run the command interpreter
    HBNBCommand().cmdloop()   

#!/usr/bin/python3
"""Defines the cmd interpreter HBnB console."""

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage



class HBNBCommand(cmd.Cmd):

    """Defines the command interpreter Class.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    
    def emptyline(self):
        """Execution of an empty line doesn't do anything."""
        pass

    def default(self, user_input):
        """Handles commands that dont match any specified ones."""       
        self.handle_cmd(user_input)

    def handle_cmd(self, user_input):
        """Defines the cmd module behavior when input is invalid"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", user_input)
        if not match:
            return user_input
        cls_name = match.group(1)
        mtd = match.group(2)
        args = match.group(3)
        match_u_a = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_u_a:
            obj_id = match_u_a.group(1)
            att_dict = match_u_a.group(2)
        else:
            obj_id = args
            att_dict = False

        att_val = ""
        if mtd == "update" and att_dict:
            match_dict = re.search('^({.*})$', att_dict)
            if match_dict:
                self.dict_update(cls_name, obj_id, match_dict.group(1))
                return ""
            match_att_val = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', att_dict)
            if match_att_val:
                att_val = (match_att_val.group(
                    1) or "") + " " + (match_att_val.group(2) or "")
        command = mtd + " " + cls_name + " " + obj_id + " " + att_val
        self.onecmd(command)
        return command

    def dict_update(self, cls_name, obj_id, s_dict):
        """Method to help update an instance based on his ID with a dictionary."""
        sd = s_dict.replace("'", '"')
        dic = json.loads(sd)
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in storage.classes():
            print("** class doesn't exist **")
        elif obj_id is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(cls_name, obj_id)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[cls_name]
                for attribute, value in dic.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_quit(self, user_input):
        """Method Quit to exit the program."""
        return True

    def do_EOF(self, user_input):
        """EOF signal to exit the program."""
        print()
        return True


    def do_create(self, user_input):
        """Method to creates a new instance of BaseModel."""
        if user_input == "" or user_input is None:
            print("** class name missing **")
        elif user_input not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[user_input]()
            b.save()
            print(b.id)

    def do_show(self, user_input):
        """Method that prints the string representation 
        of an instance based on class name and ID.
        """
        if user_input == "" or user_input is None:
            print("** class name missing **")
        else:
            strings = user_input.split(' ')
            if strings[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(strings) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(strings[0], strings[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, user_input):
        """Method that deletes an instance based 
        on the class name and ID.
        """
        if user_input == "" or user_input is None:
            print("** class name missing **")
        else:
            strings = user_input.split(' ')
            if strings[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(strings) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(strings[0], strings[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, user_input):
        """Prints all string representation of all instances 
        based or not on the class name.
        """
        if user_input != "":
            strings = user_input.split(' ')
            if strings[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                n_list = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == strings[0]]
                print(n_list)
        else:
            newList = [str(obj) for key, obj in storage.all().items()]
            print(newList)

    def do_count(self, user_input):
        """Method that Retrieve the number of instances of 
        a given class.
        """
        strings = user_input.split(' ')
        if not strings[0]:
            print("** class name missing **")
        elif strings[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    strings[0] + '.')]
            print(len(matches))

    def do_update(self, user_input):
        """Method that updates an instance based on the class name 
        and id by adding or updating attribute.
        """
        if user_input == "" or user_input is None:
            print("** class name missing **")
            return

        pattern = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(pattern, user_input)
        cls_name = match.group(1)
        obj_id = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif cls_name not in storage.classes():
            print("** class doesn't exist **")
        elif obj_id is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(cls_name, obj_id)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                t_cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        t_cast = float
                    else:
                        t_cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[cls_name]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif t_cast:
                    try:
                        value = t_cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

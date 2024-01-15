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
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.dict_update(cls_name, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + cls_name + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

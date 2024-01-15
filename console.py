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

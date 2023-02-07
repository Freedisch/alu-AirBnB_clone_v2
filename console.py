#!/usr/bin/python3
'''class cmd that defines the functions of a custom command line interpreter'''

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re


# input the class names in a dict for easier access

class_names = {
    "BaseModel":BaseModel
}
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):

        '''command to exit the program'''
        return True
    def do_quit(self, arg):

        '''exit the program'''
        sys.exit(1)
    def help_quit(self):
        print('Help command to exit the program')

    def help(self):
        print('Help command to output help instructions')

    def emptyline(self):
        '''do nothing when empty line is entered'''
        pass

#     add new functions to the CLI

    def do_create(self, cls):

        '''class name to create new basemodel instance'''
        if not cls:
            print('** class name missing **')
        elif cls not in class_names.keys():
            print("** class doesn't exist **")
        else:
            new = class_names[cls]()
            new.save()
            print(new.id)

    def do_show(self, cls_id):

        '''show string representation of instance'''
        # Break the cls_id argument
        args = cls_id.split()
        new_rep = args[0]+'.'+args[1]
        # create a variable to store all objects
        objects_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in class_names:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id is missing **")
        elif new_rep in objects_dict:
            print(objects_dict[new_rep])
        else:
            print("** no instance found **")
    def do_destroy(self, cls_id):

        '''show string representation of instance'''
        # Break the cls_id argument
        args = cls_id.split()
        new_rep = "{}.{}".format(args[0], args[1])
        # create a variable to store all objects
        objects_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in class_names:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id is missing **")
        elif new_rep not in objects_dict:
            print("** no instance found **")
        else:
            del objects_dict[new_rep]
            storage.save()

    def do_all(self, cls):
        obj_dict = storage.all()
        if not cls:
            for obj in obj_dict.values():
                print(str(obj))
        elif cls not in class_names:
            print("** class doesn't exist **")
        else:
            for key, obj in obj_dict.items():
                if key.split('.')[0] == cls:
                    print(str(obj))

    def do_update(self, args):

        '''update an object with a new value using its class name and id '''

        args_list = args.split()
        all_objs = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
            return False
        cls_name = args_list[0]

        if cls_name not in class_names.keys():
            print("** class doesn't exist ** ")
            return False

        if len(args_list) == 1:
            print("** instance id missing **")
            return False
        inst_id = args_list[1]

        ''' create a key to check for instance in storage.all'''

        obj_key = "{}.{}".format(cls_name, inst_id)

        if obj_key not in all_objs:
            print("** instance not found **")
            return False
        if len(args_list) == 2:
            print("** attribute name missing **")
            return False
        attr_name = args_list[2]

        if len(args_list) == 3:
            print("** value missing **")
            return False
        attr_value = args_list[3]

        '''update instance with new values'''
        obj = all_objs[obj_key]

        obj.__dict__.update({attr_name: attr_value})
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


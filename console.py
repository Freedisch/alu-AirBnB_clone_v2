#!/usr/bin/python3
'''class cmd that defines the functions of a custom command line interpreter'''

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        new_rep = args[0]+'.'+args[1]
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

    def do_update(self, *args):

        args_split = args.split(' ')

        if len(args_split) < 4:
            args_len = len(args_split)
            # print(args_len)
            # print(args_split)
            if not args:
                print("** class name missing **")
                return
            if args_len == 1:
                print("** instance id missing **")
                return
            if args_len == 2:
                print("** attribute name missing **")
                return
            if args_len == 3:
                print("** value missing **")
                return

        else:
            args_split = args_split[:4]

            cls_name = args_split[0]
            obj_id = args_split[1]
            attr_name = args_split[2]
            attr_value = args_split[3]

            storage = FileStorage()
            storage.reload()
            all_objects = storage.all()

            # create a key of the form <class name>.<id> to search in storage
            user_key = cls_name + '.' + obj_id

            if cls_name not in classes.keys():
                print("** class doesn't exist **")
                return
            if user_key not in all_objects.keys():
                print("** no instance found **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()


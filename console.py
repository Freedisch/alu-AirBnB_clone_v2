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

    def create(self, cls):

        '''class name to create new basemodel instance'''
        if not cls:
            print('** class name missing **')
        elif cls not in class_names.keys():
            print("** class doesn't exist **")
        else:
            new = class_names[cls]()
            new.save()
            print(new.id)

    def show(self, cls_id):

        '''show string representation of instance'''
        # Break the cls_id argument
        args = cls_id.split()
        new_rep = args[0]+'.'+args[1]
        # create a variable to store all objects
        objects_dict = storage.all()
        if len(args) == 0:
            print("**class name missing**")
        elif args[0] not in class_names:
            print("**class doesn't exist**")
        elif len(args) != 2:
            print("**instance id is missing**")
        elif new_rep in objects_dict:
            print(objects_dict[new_rep])
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()



import cmd
import sys


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

if __name__ == '__main__':
    HBNBCommand.cmdloop()

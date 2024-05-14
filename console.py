#!/usr/bin/python3
'''
module
'''


import cmd
class HBNBCommand(cmd.Cmd):
    '''
    class
    '''

    prompt="(hbnb) "

    def do_help(self, arg):
        '''
        here's ur help for this interpreter
        '''
        return super().do_help(arg)

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
        EOF to exit the program
        '''
        return True

    def emptyline(self):
        '''
        emptyline - Do NOTHING
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

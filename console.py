#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, args):
        """Handle EOF (Ctrl+D) input.

        Usage: EOF
        """
        return True
    def do_quit(self,args):
        '''Quit command to exit the program'''
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
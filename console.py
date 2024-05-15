#!/usr/bin/python3
'''
module
'''


import cmd
import shlex
from models.base_model import BaseModel
from models import storage
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

    def do_create(self, ins=None):
        '''
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        '''
        if ins is None or len(ins) == 0:
            print("** class name missing **")
        elif ins == "BaseModel":
            ins = BaseModel()
            ins.save()
            print(ins.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        '''
        Prints the string representation of an instance based on the class name and id
        '''
        arg = list(args.split())
        if arg[0] is None or len(arg[0]) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            id = arg[1]
            for key, value in storage.all().items():
                cls, ins_id = key.split(".")
                if (id == ins_id):
                    print(str(value))
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id
        '''
        arg = list(args.split())
        if arg[0] is None or len(arg[0]) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            id = arg[1]
            for key in storage.all().keys():
                cls, ins_id = key.split(".")
                if (id == ins_id):
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        '''
        Prints all string representation of all instances
        '''
        arg = list(args.split())
        if len(arg) > 1 and arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            list_all = []
            for value in storage.all().values():
                list_all.append(str(value))
            print(list_all)
    
    def do_update(self, args):
        '''
         Updates an instance based on the class name and id
        '''
        arg = shlex.split(args)
        if arg[0] is None or len(arg[0]) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            id, new_attr, new_attr_val = arg[1], arg[2], arg[3]
            new_attr_val = str(new_attr_val)
            new_attr_val = str(new_attr_val.strip('"'))
            try:
                # Try casting to integer
                new_attr_val = int(new_attr_val)
            except ValueError:
                try:
                    # Try casting to float
                    new_attr_val = float(new_attr_val)
                except ValueError:
                    # Return the string as is
                    pass
            for key, value in storage.all().items():
                cls, ins_id = key.split(".")
                if (id == ins_id):
                    setattr(value, new_attr, new_attr_val)
                    storage.save()
                    return
            print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()

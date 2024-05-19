#!/usr/bin/python3
'''
module
'''


import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
        }


class HBNBCommand(cmd.Cmd):
    '''
    class
    '''

    prompt = "(hbnb) "

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

    def do_create(self, cls=None):
        '''
        Creates a new instance of BaseModel, saves it, prints the id
        '''
        if cls is None or len(cls) == 0:
            print("** class name missing **")
        elif cls in classes:
            class_name = classes[cls]
            ins = class_name()
            ins.save()
            print(ins.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''
        Prints the string representation of an instance
        '''
        arg = list(args.split())
        if args is None or len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            cls_input, id = arg[0], arg[1].replace('"', '')
            for key, value in storage.all().items():
                cls, ins_id = key.split(".")
                if cls == cls_input and id == ins_id:
                    print(str(value))
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id
        '''
        arg = list(args.split())
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            cls_input, id = arg[0], arg[1].replace('"', '')
            for key in list(storage.all().keys()):
                cls, ins_id = key.split(".")
                if cls == cls_input and id == ins_id:
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
        if len(arg) > 1 and (arg[0] not in classes):
            print("** class doesn't exist **")
        else:
            list_all = []
            if (len(arg) < 1):
                for key, value in storage.all().items():
                    list_all.append(str(value))
            else:
                for key, value in storage.all().items():
                    cls, ins_id = key.split(".")
                    if cls == arg[0]:
                        list_all.append(str(value))
            print(list_all)

    def do_update(self, args):
        '''
         Updates an instance based on the class name and id
        '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            cls_input, id = arg[0], arg[1]
            new_attr, new_attr_val = arg[2], arg[3]
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
                if cls == cls_input and ins_id == id:
                    setattr(value, new_attr, new_attr_val)
                    storage.save()
                    return
            print("** no instance found **")

    def default(self, line):
        '''
        defualt
        '''
        args = line.split('.')
        if len(args) == 1:
            return super().default(line)
        action = args[1]
        correct_action = action.split('(')[0]
        if action == "all()":
            self.do_all(args[0])
        elif action == "count()":
            self.do_count(args[0])
        elif correct_action == "show":
            id = ''.join(action.split('(')[1:])
            id = id.replace(')', '')
            id = id.replace('"', '')
            final = args[0] + " " + id
            self.do_show(final)
        elif correct_action == "destroy":
            id = ''.join(action.split('(')[1:])
            id = id.replace(')', '')
            id = id.replace('"', '')
            final = args[0] + " " + id
            self.do_destroy(final)
        else:
            return super().default(line)

    def do_count(self, args):
        '''
        count no o finstances
        '''
        arg = list(args.split())
        if arg[0] is None or len(arg[0]) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            cls_input = arg[0]
            num = 0
            for key in storage.all().keys():
                cls, ins_id = key.split(".")
                if cls == cls_input:
                    num += 1
            print(num)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/bin/bash/python3

import cmd
from models.base_model import BaseModel

''' This the console module '''

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Quit command to exit the program."""
        print("")
        return True

    
    def emptyline(self):
        """Do nothing on empty line."""
        pass 

    def do_create(self, line):
        '''Create model instance if class name is valid'''

        if not line:
            print("** class name missing **")
            return

        approved_classes = ['BaseModel', 'User']
        args = line.split()
        class_name = args[0]
        
        if class_name in approved_classes:
            ''' Dynamically retrieve the class type from globals() '''
            class_type = globals().get(class_name)
            if class_type is not None:
                obj = class_type()
                obj.save()
                print(obj.id)
        else:
            print("** class doesn't exist **")

#     show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
# If the class name is missing, print ** class name missing ** (ex: $ show)
# If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
# If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
# If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        
        approved_classes = ['BaseModel', 'User']
        args = line.split()
        class_name = args[0]
        class_id = args[1]
        class_types = []
        if class_name in approved_classes:
            class_type = globals().get(class_name)
            if class_type is not None:
                class_types.append(class_type)
                return
        else:
            print("** class doesn't exist **")
        if class_id:
            pass






if __name__ == '__main__':
    HBNBCommand().cmdloop()

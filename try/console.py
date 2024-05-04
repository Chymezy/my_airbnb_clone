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

        


                
        #     if class_name and issubclass(obj_class, BaseModel):
        #     if class_name in class_list:
        #         obj = BaseModel()
        #         obj.save()
        #         print(obj.id)
        #     else:
        #         print("** class doesn't exist **")
        # r = ['BaseModel', 'User']
        # a = eval(r[0])
        # print(type(a))       
                
                



 
        # instance = BaseModel()
        # instance.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()

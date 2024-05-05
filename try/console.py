#!/bin/bash/python3

import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, line):
        ''' retrieve and display object data '''
        if not line:
            print("** class name missing **")
            return
        else:

            approved_classes = ['BaseModel', 'User']
            args = line.split()
            ''' check class '''
            if len(args) > 0: #True
                class_name = args[0] # BaseModel
                class_types = [] #'<model.base_model.BaseModel>'
                if class_name in approved_classes:
                    class_type = globals().get(class_name) #'<model.base_model.BaseModel>'
                    if class_type is not None:
                        class_types.append(class_type)

                    ''' check id '''    
                    if len(args) > 1:    
                        class_id = args[1] 
                        if class_id:
                            all_objs = storage.all()
                            ids = []
                            for obj_id in all_objs.keys():
                                ids.append(obj_id.split('.')[1])
                            if class_id in ids:
                                key = f'{class_name}.{class_id}'
                                print(all_objs[key])
                                return
                            else:
                                print("** no instance found **")
                                return
                    else:
                        print('** instance id missing **')
                        return
            else:
                print("** class doesn't exist **")
                return



if __name__ == '__main__':
    HBNBCommand().cmdloop()

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
    def validate_input(self, args, approved_classes, require_id=False):
        if not args:
            print("** class name missing **")
            return False, None, None
        else:
            class_name = args[0]
            if class_name not in approved_classes:
                print("** class doesn't exist **")
                return False, None, None
            else:
                class_type = globals().get(class_name)
                if class_type is None:
                    print("** class doesn't exist **")
                    return False, None, None
                if require_id and len(args) < 2:
                    print('** instance id missing **')
                    return False, None, None
                class_id = args[1] if len(args) > 1 else None
        return True, class_name, class_id

    def do_create(self, line):
        """Create command to create new instance"""
        approved_classes = ['BaseModel']
        args = line.split()
        valid_input, class_name, _ = self.validate_input(args, approved_classes)
        if valid_input:
            new_instance = globals()[class_name]()
            new_instance.save()

    def do_show(self, line):
        """Show command to print instance details"""
        approved_classes = ['BaseModel']
        args = line.split()
        valid_input, class_name, class_id = self.validate_input(args, approved_classes, require_id=True)
        if valid_input:
            all_objs = storage.all()
            key = f"{class_name}.{class_id}"
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy command to delete instance"""
        approved_classes = ['BaseModel']
        args = line.split()
        valid_input, class_name, class_id = self.validate_input(args, approved_classes, require_id=True)
        if valid_input:
            all_objs = storage.all()
            key = f"{class_name}.{class_id}"
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        ''' Displays all created objects '''
        obj_list = []

        ''' Function to display all objects '''
        def display_objects():
            all_objs = storage.all()
            for obj in all_objs.values():
                obj_str = f'{obj.__class__.__name__} ({obj.id}) {obj.__dict__}'
                obj_list.append(obj_str)
            print(obj_list)

        if not line:    # if line is empty
            display_objects() 
        else:
            ''' validate line if not empty '''
            approved_classes = ['BaseModel']
            args = line.split()
            valid_input, _, _ = self.validate_input(args, approved_classes)
            if valid_input:
                # After input validation, display all objects
                display_objects()




if __name__ == '__main__':
    HBNBCommand().cmdloop()


#     def do_create(self, line):
#         '''Create model instance if class name is valid'''

#         if not line:
#             print("** class name missing **")
#             return

#         approved_classes = ['BaseModel', 'User']
#         args = line.split()
#         class_name = args[0]
        
#         if class_name in approved_classes:
#             ''' Dynamically retrieve the class type from globals() '''
#             class_type = globals().get(class_name)
#             if class_type is not None:
#                 obj = class_type()
#                 obj.save()
#                 print(obj.id)
#         else:
#             print("** class doesn't exist **")

#     def do_show(self, line):
#         ''' retrieve and display object data '''
#         if not line:
#             print("** class name missing **")
#             return
#         else:

#             approved_classes = ['BaseModel', 'User']
#             args = line.split()
#             ''' check class '''
#             if len(args) > 0: #True
#                 class_name = args[0] # BaseModel
#                 class_types = [] #'<model.base_model.BaseModel>'
#                 if class_name in approved_classes:
#                     class_type = globals().get(class_name) #'<model.base_model.BaseModel>'
#                     if class_type is not None:
#                         class_types.append(class_type)

#                     ''' check id '''    
#                     if len(args) > 1:    
#                         class_id = args[1] 
#                         if class_id:
#                             all_objs = storage.all()
#                             ids = []
#                             for obj_id in all_objs.keys():
#                                 ids.append(obj_id.split('.')[1])
#                             if class_id in ids:
#                                 key = f'{class_name}.{class_id}'
#                                 print(all_objs[key])
#                                 return
#                             else:
#                                 print("** no instance found **")
#                                 return
#                     else:
#                         print('** instance id missing **')
#                         return
#             else:
#                 print("** class doesn't exist **")
#                 return

# #     destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
# # If the class name is missing, print ** class name missing ** (ex: $ destroy)
# # If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
# # If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
# # If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
#     def do_destroy(self, line):
#         if not line:
#             print("** class name missing **")
#             return
#         else:
#             approved_classes = ['BaseModel', 'User']  # List of approved classes
#             args = line.split()
#             if len(args) > 0:
#                 class_name = args[0]  # Get class name
#                 if class_name in approved_classes:
#                     class_type = globals().get(class_name)  # Get class type
#                     if class_type is not None:
#                         if len(args) > 1:
#                             class_id = args[1]  # Get instance id
#                             if class_id:
#                                 all_objs = storage.all()
#                                 ids = [obj_id.split('.')[1] for obj_id in all_objs.keys()]
#                                 if class_id in ids:
#                                     key = f'{class_name}.{class_id}'
#                                     del all_objs[key]  # Delete instance
#                                     storage.save()  # Save changes to JSON file
#                                     return
#                                 else:
#                                     print("** no instance found **")
#                                     return
#                             else:
#                                 print('** instance id missing **')
#                                 return
#                         else:
#                             print('** instance id missing **')
#                             return
#                 else:
#                     print("** class doesn't exist **")
#                     return
#             else:
#                 print("** class name missing **")
#                 return




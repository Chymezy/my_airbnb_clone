import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    approved_classes = ['BaseModel', 'User', 'Amenity', 'City', 'Place', 'Review', 'State']  # Define approved classes as a class variable

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
        args = line.split()
        valid_input, class_name, _ = self.validate_input(args, HBNBCommand.approved_classes)
        if valid_input:
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Show command to print instance details"""
        args = line.split()
        valid_input, class_name, class_id = self.validate_input(args, HBNBCommand.approved_classes, require_id=True)
        if valid_input:
            all_objs = storage.all()
            key = f"{class_name}.{class_id}"
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy command to delete instance"""
        args = line.split()
        valid_input, class_name, class_id = self.validate_input(args, HBNBCommand.approved_classes, require_id=True)
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
            args = line.split()
            valid_input, _, _ = self.validate_input(args, HBNBCommand.approved_classes)
            if valid_input:
                # After input validation, display all objects
                display_objects()

    def do_update(self, line):
        """Update command to update an instance attribute"""
        args = line.split()
        valid_input, class_name, instance_id = self.validate_input(args, HBNBCommand.approved_classes, require_id=True)
        if not valid_input:
            return

        ''' Check if the instance exists '''
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        ''' Check if attribute name and value are provided '''
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        attr_name = args[2]
        attr_join = ' '.join(args[3:])  # Join attribute value if it contains spaces
        if type(attr_join) is str:
            attr_value = attr_join.strip('"')

        ''' Check if attribute exists in the instance '''
        obj = all_objs[key]
        if not hasattr(obj, attr_name):
            print("** attribute doesn't exist **")
            return
        
        ''' Update the attribute and save '''
        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        args = line.split('.')
        if len(args) == 2 and args[1] == 'all()':
            class_name = args[0]
            if class_name in HBNBCommand.approved_classes:
                class_type = globals().get(class_name)
                if class_type is not None:
                    all_instances = class_type.all()
                    for instance in all_instances:
                        print(instance)
                    return
        super().default(line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()

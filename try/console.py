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
    approved_classes = ['BaseModel', 'User', 'Amenity', 'City', 'Place', 'Review', 'State']  

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

    def validate_args(self, args): 
        if not args:
            print('** Invalid command **')
            return False, None, None             
        split_args = args[0].split('.')
        if len(split_args) != 2:
            print('** Invalid command entered **')
            return False, None, None
        class_name, method = split_args
        return True, class_name, method
   
    def display_objects(self, class_name, *args):
        obj_list = []
        all_objs = storage.all()
      
        for obj in all_objs.values():
            obj_dict = obj.to_dict()
            if obj.__class__.__name__ == class_name:
                obj_str = f"[{class_name}] ({obj.id}) {obj_dict}"
                obj_list.append(obj_str)

            elif class_name == '':
                obj_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj_dict}"
                obj_list.append(obj_str)

        if class_name and 'count' in args:
            return len(obj_list)
        else:
            print('[{}]'.format(', '.join(obj_list)))
       
    def do_create(self, line):
        args = line.split()
        valid_input, class_name, _ = self.validate_input(args, HBNBCommand.approved_classes)
        if valid_input:
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
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
        if not line:
            self.display_objects(line)
        else:
            args = line.split() 
            valid_input, class_name, _ = self.validate_input(args, HBNBCommand.approved_classes)
            if valid_input:
                self.display_objects(class_name)

    def do_update(self, line):
        args = line.split()
        valid_input, class_name, instance_id = self.validate_input(args, HBNBCommand.approved_classes, require_id=True)
        if not valid_input:
            return

        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        attr_name = args[2]
        attr_join = ' '.join(args[3:])
        if type(attr_join) is str:
            attr_value = attr_join.strip('"')

        obj = all_objs[key]
        if not hasattr(obj, attr_name):
            print("** attribute doesn't exist **")
            return
        
        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        if not line:
            print("** command missing **")
            return
        args = line.split()
        
        valid_args, class_name, method = self.validate_args(args)
        if valid_args:
            if method == 'all()':
                self.do_all(class_name)
            
            elif method == 'count()':
                if class_name not in HBNBCommand.approved_classes:
                    print("** class does not exist **")
                    return
                count = self.display_objects(class_name, 'count')
                print(count)  

            elif method.startswith('show("') and method.endswith('")'):
                obj_id = method.split('"')[1]
                self.do_show(f"{class_name} {obj_id}")
            
            elif method.startswith('destroy("') and method.endswith('")'):
                obj_id = method.split('"')[1]
                self.do_destroy(f'{class_name} {obj_id}')
            
            elif method.startswith('update("') and method.endswith('")'):
                args = method.split('"')[1:-1]  
                if len(args) != 3:
                    print("** Invalid command format for update **")
                    return
                else:
                    update_id, attr_name, attr_value = args
                    self.do_update(f"{class_name} {update_id} {attr_name} {attr_value}")
            else:
                print("** Invalid command entered **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
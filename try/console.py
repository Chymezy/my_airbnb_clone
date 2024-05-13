import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State

PROMPT = '(hbnb) '
CLASS_NAME_MISSING = '** class name missing **'
CLASS_DOES_NOT_EXIST = '** class doesn\'t exist **'
INSTANCE_ID_MISSING = '** instance id missing **'
ATTRIBUTE_NAME_MISSING = '** attribute name missing **'
ATTRIBUTE_VALUE_MISSING = '** value missing **'
ATTRIBUTE_DOES_NOT_EXIST = '** attribute doesn\'t exist **'

class HBNBCommand(cmd.Cmd):
    prompt = PROMPT
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

    def validate_input(self, args: list, approved_classes: list, require_id: bool = False) -> tuple:
        if not args:
            print(CLASS_NAME_MISSING)
            return False, None, None
        class_name = args[0]
        if class_name not in approved_classes:
            print(CLASS_DOES_NOT_EXIST)
            return False, None, None
        class_type = globals().get(class_name)
        if class_type is None:
            print(CLASS_DOES_NOT_EXIST)
            return False, None, None
        if require_id and len(args) < 2:
            print(INSTANCE_ID_MISSING)
            return False, None, None
        class_id = args[1] if len(args) > 1 else None
        return True, class_name, class_id

    def validate_args(self, args: list) -> tuple:
        if not args:
            print('** Invalid command **')
            return False, None, None
        split_args = args[0].split('.')
        if len(split_args) != 2:
            print('** Invalid command entered **')
            return False, None, None
        class_name, method = split_args
        return True, class_name, method

    def display_objects(self, class_name: str, *args) -> None:
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
            print(len(obj_list))
        else:
            print('[{}]'.format(', '.join(obj_list)))

    def do_create(self, line: str) -> None:
        args = line.split()
        valid_input, class_name, _ = self.validate_input(args, HBNBCommand.approved_classes)
        if valid_input:
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line: str) -> None:
        args = line.split()
        valid_input, class_name, class_id = self.validate_input(args, HBNBCommand.approved_classes, require_id=True)
        if valid_input:
            all_objs = storage.all()
            key = f"{class_name}.{class_id}"
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line: str) -> None:
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

    def do_all(self, line: str) -> None:
        if not line:
            self.display_objects(line)
        else:
            args = line.split()
            valid_input, class_name, _ = self.validate_input(args, HBNBCommand.approved_classes)
            if valid_input:
                self.display_objects(class_name)

    def do_update(self, class_name: str, instance_id: str, attr: str, attr_value: str) -> None:
        print(attr_value)
        if class_name not in HBNBCommand.approved_classes:
            print(CLASS_DOES_NOT_EXIST)
            return

        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if not attr:
            print(ATTRIBUTE_NAME_MISSING)
            return

        if not attr_value:
            print(ATTRIBUTE_VALUE_MISSING)
            return

        # attr_value1 = attr_value.strip(' ')
        attr_value_words = attr_value.split(' ')[0]
        print(attr_value) #debugging print
        print(attr_value_words) #debugging print
        attr_value_spaced = ' '.join(attr_value_words)
        # attr_value_spaced = {word: "" for word in attr_value_words}

        obj = all_objs[key]

        if not hasattr(obj, attr):
            print(ATTRIBUTE_DOES_NOT_EXIST)
            return

        setattr(obj, attr, attr_value_spaced)
        obj.save()

    def default(self, line: str) -> None:
        if not line:
            print("** command missing **")
            return

        args = line.replace(" ", '').split(' ')

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
                self.do_destroy(f"{class_name} {obj_id}")

            elif method.startswith('update("') and method.endswith('")'):
                args = method.split('"')[1:-1]
                print(args) #deugging print
                update_id = args[0]
                attr = args[2]
                attr_value = args[4]
                print(attr_value) #debugging print

                if not update_id and attr and attr_value:
                    print("** Invalid command format for update **")
                    return
                else:
                    update_class = line.split('.')[0]
                    self.do_update(update_class, update_id, attr, attr_value)

            else:
                print("** Invalid command entered **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
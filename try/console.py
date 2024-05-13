import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class Console(cmd.Cmd):
    """
    A command line interpreter for managing objects in a storage engine.
    """
    prompt = "(hbnb) "
    classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, class_name):
        """
        Creates a new instance of a class and saves it to the storage engine.
        """
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, class_name, instance_id):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        print(obj)

    def do_destroy(self, class_name, instance_id):
        """
        Deletes an instance based on the class name and id and saves the change to the storage engine.
        """
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, class_name):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        all_objs = storage.all()
        if class_name:
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            objs = [str(obj) for obj in all_objs.values() if isinstance(obj, self.classes[class_name])]
        else:
            objs = [str(obj) for obj in all_objs.values()]
        print(objs)

    def do_update(self, class_name, instance_id, attr, attr_value):
        """
        Updates an instance based on the class name and id by adding or updating attribute and saves the change to the storage engine.
        """
        all_objs = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        if not hasattr(obj, attr):
            print("** attribute doesn't exist **")
            return
        setattr(obj, attr, attr_value)
        obj.save()

    def default(self, line):
        """
        Handles invalid commands.
        """
        print("*** Unknown syntax: {}".format(line))

    def emptyline(self):
        """
        Handles empty lines.
        """
        pass

    def do_quit(self, line):
        """
        Quits the console.
        """
        return True

if __name__ == '__main__':
    Console().cmdloop()

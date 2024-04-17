#!/usr/bin/python3
import cmd
from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity as amenity
from models.city import City as city
from models.place import Place as place
from models.review import Review as review
from models.state import State as state
from models.user import User as user




class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB Clone"""
    prompt = "(hbnb)"
    __classes = {"User": user, "Place": place, "Review": review, "State": state, "City": city, "Amenity": amenity}

    def do_create(self, args):
      """Creating a new instance of the create class with given parameters"""
      args = args.split()

      if len(args) < 1:
        print("**class name missing**")
        return
      class_name = args[0]

      if class_name not in self.__classes:
        print("**class name doesn't exist**")
        return

      # Remove the class name from the arguments
      args = args[1:]

      # Initialize an empty dictionary to hold the parameters
      kwargs = {}

      # Parse the parameters and add them to the kwargs dictionary
      for arg in args:
        key_value = arg.split("=")
        if len(key_value) != 2:
            print(f"Skipping invalid parameter: {arg}")
            continue
        key, value = key_value
        # Replace underscores with spaces in the key
        key = key.replace("_", " ")
        # Replace escaped double quotes with regular double quotes in the value
        value = value.replace('\\"', '"')
        # Add the parameter to the kwargs dictionary
        kwargs[key] = value

     # Create a new instance of the class with the given parameters
      new_instance = self.__classes[class_name](**kwargs)
      new_instance.save()
      print(new_instance.id)


    def do_show(self, args):
        """Showing string representation of an instance"""

        args = args.split()

        if len(args) < 2:
            print("**instance is missing**")
            return
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in file_storage.all():
            print("**no instance is found**")
            return
        print(file_storage.all()[key])

    def do_update(self, args):
        """Updating an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            key = args[0] + "." + args[1]
            if key not in file_storage.all():
                print("** no instance found **")
                return
            obj = file_storage.all()[key]
            setattr(obj, args[2], args[3])
            obj.save()
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        
        print("")  # Printing newline before exiting
        return True

    def emptyline(self,args):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
    






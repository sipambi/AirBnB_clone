#usr/bin/python3
"""
    File Storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
        Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place, "Amenity": Amenity, "City": City, "Review": Review, "State": State}
    #comeback and add class_dict when the time comes
    
    def all(self):
        """
            Returns a dictionary of objects
        """
        return self.__objects
    
    def new(self, obj):
        """
            add new object to existing dictionary of instances
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
        
    def save(self):
        """Serializes objects to json file
        """
        my_dict = {}
        
        for key, obj in self.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else:'''
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)
            
        def reload(self):
            """Deserialise the JSON file to __objects if the JSON file exists
            """
            try:
                with open(self.__file_path, 'r') as f:
                    new_obj = json.load(f)
                for key, val in new_obj.items():
                    obj = self.class_dict[val['__class__']](**val)
                    self.__objects[key] = obj
            except FileNotFoundError:
                pass
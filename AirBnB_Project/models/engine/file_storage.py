import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key_dict = obj.__class__.__name__+"."+obj.id
        self.__objects.update({key_dict: obj})

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as sve:
            temp_dict = {}
            for keys, value in self.__objects.items():
                temp_dict.update({keys: value.to_dict()})
            json.dump(temp_dict, sve)

    def reload(self):
        if not os.path.isfile(self.__file_path):
            return

        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        from models.base_model import BaseModel
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            j_file = json.load(f)

        for key, value in j_file.items():
            class_name, obj_id = key.split('.')
            get_me = eval(class_name)  # Get the class by name
            obj = get_me(**value)  # Create an instance of the class using the data
            self.new(obj)


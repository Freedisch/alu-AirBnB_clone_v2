#!/usr/bin/python
''' new class filestorage that stores new objects in a json file'''

import json
import os

class FileStorage:
    ''' class filestorage, serializes object instance.
    The class will also deserialize Json files into instances
     private class attributes'''

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''class constructor'''
        pass

    def all(self):
        ''' return the dictionary rep of objects'''
        return self.__objects

    def new(self, obj):
        ''' input the new object into __objects.'''
        ''' classname.id is the key and obj name is value'''

        cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        '''serialize new object into __file_path'''
        dictionary = {}
        for obj in FileStorage.__objects:
            dictionary[obj] = FileStorage.__objects[obj].to_dict()
        with open(self.__file_path, "w") as new_file:
            json.dump(dictionary, new_file)
        #my_obj_dict = {}
        #for key in FileStorage.__objects:
            #my_obj_dict[key] = FileStorage.__objects[key].to_dict()
        # with open(FileStorage.__file_path, 'w') as file_path:
        #     json.dump(my_obj_dict, file_path)

    def reload(self):
        '''deserializes the json file (__file_path) to t
        the __objects dictionary'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity

        test_dict = {
            "User": User,
            "State": State,
            "City": City,
            "Review": Review,
            "Place": Place,
            "Amenity": Amenity
        }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as test_dict:
            dictionary = json.load(test_dict)
            FileStorage.__objects = {}
            for item in dictionary:
                # cls_name = item['__class__']
                # self.new(eval(cls_name + "(**" + str(item) + ")"))
                cls_name = item.split(".")[0]
                FileStorage.__objects[item] = test_dict[cls_name](**dictionary[item])

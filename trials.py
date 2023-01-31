from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

if len(kwargs) != 0:
    for key, value in kwargs.items():
        if key == "__class__":
            continue
        if key == "created_at" or key == "updated_at":
            self.__dict__[key] = datetime.strptime(value, datetime_obj)
        else:
            setattr(self, key, value)
        else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)



# filestorage


''' new class filestorage that stores new objects in a json file'''

import json


class FileStorage:
    ''' class filestorage that will serialize instances of an object into a Json file.
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
        for obj in self.__objects:
            dictionary[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, "w") as new_file:
            json.dump(dictionary, new_file)

    def reload(self):

        '''deserializes the json file (__file_path) to t
        the __objects dictionary'''
        from models.base_model import BaseModel

        try:
            with open(self.__file_path) as f:
                dictionary = json.load(f)
                for item in dictionary.values():
                    cls_name = item['__class__']
                    self.new(eval(cls_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass

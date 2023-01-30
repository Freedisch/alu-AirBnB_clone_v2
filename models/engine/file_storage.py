''' new class filestorage that stores new objects in a json file''' 


import json


''' class filestorage that will serialize instances of an object into a Json file. 
The class will also deserialize Json files into instances'''


class FileStorage: 
    
    ''' private class attributes''' 
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

        ocname = obj.__class__.__name__
        self.__objects["{}.{}".format(ocname, obj.id)] = obj
    def save(self):
        
        '''serialize new object into __file_path'''
        dictionary = {}
        for obj in self.__objects:
            dictionary[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, "w") as new_file:
            json.dump(dictionary, new_file)
    def reload(self):
        from models.base_model import BaseModel
        '''deserializes the json file (__file_path) to t
        the __objects dictionary'''

        try:
            with open(self.__file_path, 'r') as f: 
                dictionary = json.load(f)
                for item in dictionary.values():
                    cls_name = item['__class__']
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            pass
    
        
     





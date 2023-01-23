''' new class filestorage that stores new objects in a json file''' 


import models
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
        k = obj.__class__.__name__ + "." +obj.id
        self.__objects.update({k: obj})
    
    def save(self):
        
        '''serialize new object into __file_path'''
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w") as new_file:
            json.dump(dictionary, new_file)
    def reload(self): 
        
        '''deserializes the json file (__file_path) to t
        the __objects dictionary''' 
        try:
            with open(self.__file_path, 'r') as f: 
                dictionary = json.loads(f)
                for key, value in dictionary.items():
                    self.__objects[key] = value
        except:
            pass
    
        
     





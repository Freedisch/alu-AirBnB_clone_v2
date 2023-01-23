

''' class BaseModel that defines all common attributes/methods for other classes:'''

import uuid
from datetime import datetime
import json
from models import storage

class BaseModel:
    ''' defines all common attributes/methods for other classes:'''

    def __init__(self, *args, **kwargs):
        
        ''' Initialise the Basemodel'''
        if kwargs: 
            datetime_obj = "%Y-%m-%dT%H:%M:%S.%f"
            if len(kwargs) == 0:
                for key, value in kwargs.items(): 
                    if key == "__class__":
                        continue
                    if key == "created_at" or Key == "updated_at":
                        value = datetime.strptime(value, datetime_obj)
                    setattr(self, key, value)
        else: 
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def __str__(self):
        ''' string representation of object'''
        name = type(self).__name__
        number = self.id
        dictionary = self.__dict__
        return f'[{name}] ({number}) {dictionary}'

    def save(self):
        ''' update the date of module update to current date'''
        new_time = datetime.now().isoformat()
        return new_time
        storage.save()

    def to_dict(self):
        ''' append basemodel with classname print the dictionary of basemodel'''
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        dictionary = self.__dict__
        name = type(self).__name__
        dictionary["__class__"] = name
        return self.__dict__



obj = BaseModel()
new = (obj.__class__.__name__ + "." +obj.id)

fn = "file.json" 
dictionary1 = {new:obj}
# print(dictionary1)
dictionary2 = {}
for key, value in dictionary1.items():
    dictionary2[key] = value.to_dict()
with open(fn, "w") as n:
    json.dump(dictionary2, n)
with open(fn, "r") as f:
    print(f.read()) 



#!/usr/bin/python3

''' class BaseModel that defines all common attributes/methods for other classes:'''

import uuid
from datetime import datetime
import models
class BaseModel:
    ''' defines all common attributes/methods for other classes:'''

    def __init__(self, *args, **kwargs):
        
        ''' Initialise the Basemodel'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
           datetime_obj = "%Y-%m-%dT%H:%M:%S.%f"
           kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], datetime_obj)
           kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], datetime_obj)
           del kwargs["__class__"]
           self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
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


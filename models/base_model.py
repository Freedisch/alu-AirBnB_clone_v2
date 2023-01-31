#!/usr/bin/python3

''' class BaseModel that defines all common attributes/methods for other classes:'''

import uuid
from datetime import datetime
import models


class BaseModel:
    ''' defines all common attributes/methods for other classes:'''

    def __init__(self, *args, **kwargs):
        
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            kwargs["created_at"] = datetime.strftime(kwargs["created_at"], time_form)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], time_form)
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.crated_at = datetime.now()
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' append basemodel with classname print the dictionary of basemodel'''
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        dictionary = self.__dict__
        name = type(self).__name__
        dictionary["__class__"] = name
        return dictionary

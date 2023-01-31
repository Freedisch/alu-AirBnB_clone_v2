#!/usr/bin/python3

''' class BaseModel that defines all common attributes/methods for other classes:'''

import uuid
from datetime import datetime
import models


class BaseModel:
    ''' defines all common attributes/methods for other classes:'''

    def __init__(self, *args, **kwargs):

        ''' Initialise the Basemodel'''
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

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
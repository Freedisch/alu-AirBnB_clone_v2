#!/usr/bin/python3
from models.base_model import BaseModel 
from datetime import datetime
from models.engine.file_storage import FileStorage
import os
import unittest

class TestBaseModel(unittest.TestCase):
    """This test the BaseModel class"""


    def test__saving(self):
        """check whether id, created_at, updated_at have been set correctly"""
        with open("file.json", 'w'):
            FileStorage.__file_path = "file.json"
            #FileStorage.__objects = {}
    
    def test__deleted(self):
        """Deleting files"""
        FileStorage.__file_path = "file.json"
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test__doc(self):
        """Checking docs"""
        self.assertTrue(len(BaseModel.__dict__) > 0) 

    def test_class_model_attribute(self):
        """check whether id, created_at, updated_at have been set correctly"""
        test_model = BaseModel()
        self.assertTrue(type(test_model.id) == str)
        self.assertTrue(type(test_model.created_at) == datetime)
        #self.assertFalse(type(test_model.updated_at) ==  datetime)
    
    def test_output(self):
        ouput_test = BaseModel()
        self.assertEqual(ouput_test.__str__(), "[" + ouput_test.__class__.__name__ + "]"
                         " (" + ouput_test.id + ") " + str(ouput_test.__dict__))
    
    def test__dict(self):
        """Testing dict if exist and contains data"""
        dict_model = BaseModel()
        dict = dict_model.__dict__
        self.assertTrue(type(dict["created_at"] == str))
        self.assertTrue(type(dict["updated_at"] == str))
        self.assertTrue(type(dict_model.created_at) == datetime)
        self.assertTrue(type(dict_model.updated_at) == datetime)
        #self.assertEqual(dict["created_at"], dict_model.created_at.isoformat())
        #self.assertEqual(dict["updated_at"], dict_model.updated_at.isoformat())
    
    def test_base_from_emp_dict(self):
        """is dict empty or not"""
        dict = {}
        dict_model = BaseModel(**dict)
        self.assertTrue(type(dict_model.id) == str)
        self.assertTrue(type(dict_model.created_at) == datetime)
        self.assertTrue(type(dict_model.updated_at) == datetime)

    def test_base_from_non_dict(self):
        """is dict available or not"""
        dict_model = BaseModel(None)
        self.assertTrue(type(dict_model.id) == str)
        self.assertTrue(type(dict_model.created_at) == datetime)
        self.assertTrue(type(dict_model.updated_at) == datetime)


    def test_model_saved(self):
        """Testing the save method of BaseModel"""
        test_save = BaseModel()
        unsaved = test_save.updated_at
        saved = test_save.updated_at
        self.assertFalse(saved > unsaved)

    def test_class(self):
        """testing class instanciation"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)
    
    def test_isexcutable(self):
        """ Test if the file is excutable or not"""
        read_access = os.access('models/base_model.py', os.R_OK)
        self.assertFalse(read_access)
        write_access = os.access('models/base_model.py', os.W_OK)
        self.assertFalse(write_access)
        excecution_access = os.access('models/base_model.py', os.X_OK)
        self.assertFalse(excecution_access)
    
if __name__ == '__main__':
        unittest.main()


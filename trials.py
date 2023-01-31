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
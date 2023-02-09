
from models.base_model import BaseModel


class Amenity(BaseModel):

    '''class amenity that inherits from BaseModel'''

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
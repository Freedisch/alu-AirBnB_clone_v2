from models.base_model import BaseModel


class City(BaseModel):

    '''class state that inherits from BaseModel'''

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

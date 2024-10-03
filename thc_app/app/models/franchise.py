from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class Franchise(BaseModel):
    id = IntegerField(pk=True)
    name = CharField()
    slug = CharField()
    url = CharField()
    
    class Meta:
        schema = 'games'
        table = 'franchise'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Franchise(id={self.id}, name={self.name}"
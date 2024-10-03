from django.db.models import *


from api.app.models.base_model import BaseModel
from api.app.models.games import Game


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
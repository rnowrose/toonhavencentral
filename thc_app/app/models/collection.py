from django.db.models import *

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class Collection(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    slug = CharField(max_length=255)
    type = ForeignKey('CollectionType', related_name='collection_types')
    url = CharField(max_length=255)
    
    class Meta:
        schema = 'games'
        table = 'collection'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
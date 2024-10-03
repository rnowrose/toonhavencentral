from django.db.models import *

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionType(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    description = TextField()

    
    class Meta:
        schema = 'games'
        table = 'collection_type'
        table_description = 'Enums for collection types'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
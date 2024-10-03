from api.app.models.base_model import BaseModel
from api.app.models.games import Game
from django.db.models import *

class CollectionRelation(BaseModel):
    id = IntegerField(pk=True)
    parent_collection = ForeignKey('Collection', related_name='parent_collections')
    child_collection = ForeignKey('Collection', related_name='child_collections')
    type = ForeignKey('CollectionRelatonType', related_name='collection_relation_type')
    
    class Meta:
        schema = 'games'
        table = 'collection_relation'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
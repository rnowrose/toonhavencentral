from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class CollectionMembershipType(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    description = TextField()
    allowed_collection_type = ForeignKey('CollectionType', related_name='collection_types')

    
 
    class Meta:
        schema = 'games'
        table = 'collection_membership_type'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
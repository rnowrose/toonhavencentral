from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionMembershipType(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    allowed_collection_type = fields.ForeignKeyField('CollectionType', related_name='collection_types')

    
 
    class Meta:
        schema = 'games'
        table = 'collection_membership_type'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
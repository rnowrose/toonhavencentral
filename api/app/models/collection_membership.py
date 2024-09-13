from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionMembership(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=255)
    collection = fields.ForeignKeyField('Collection', related_name='collections')
    game = fields.ForeignKeyField('Game', related_name='game')
    type = fields.ForeignKeyField('CollectionMembershipType', related_name='collection_membership_type')
    url = fields.CharField(max_length=255)
    
    class Meta:
        schema = 'games'
        table = 'collection'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionRelation(BaseModel):
    id = fields.IntField(pk=True)
    parent_collection = fields.ForeignKeyField('Collection', related_name='parent_collections')
    child_collection = fields.ForeignKeyField('Collection', related_name='child_collections')
    type = fields.ForeignKeyField('CollectionRelatonType', related_name='collection_relation_type')
    
    class Meta:
        schema = 'games'
        table = 'collection_relation'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
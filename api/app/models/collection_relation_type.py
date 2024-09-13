from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionRelationType(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    allowed_child_type = fields.ForeignKeyField('CollectionType', related_name='parent_collection_types')
    allowed_parent_type = fields.ForeignKeyField('CollectionType', related_name='child_collection_types')

    class Meta:
        schema = 'games'
        table = 'collection_relation_type'
        table_description = 'Collection Relation Types'    
    
    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
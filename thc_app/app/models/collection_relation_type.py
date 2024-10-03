from django.db.models import *

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class CollectionRelationType(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    description = TextField()
    allowed_child_type = ForeignKey('CollectionType', related_name='parent_collection_types')
    allowed_parent_type = ForeignKey('CollectionType', related_name='child_collection_types')

    class Meta:
        schema = 'games'
        table = 'collection_relation_type'
        table_description = 'Collection Relation Types'    
    
    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class Collection(BaseModel):
    id = fields.IntField(pk=True)
    games = fields.ReverseRelation["Game"]
    name = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=255)
    type = fields.ForeignKeyField('CollectionType', related_name='collection_types')
    url = fields.CharField(max_length=255)
    
    class Meta:
        schema = 'games'
        table = 'collection'
        table_description = 'Game Data'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
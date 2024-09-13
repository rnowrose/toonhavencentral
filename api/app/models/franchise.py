from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class Franchise(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField()
    slug = fields.CharField()
    url = fields.CharField()
    
    class Meta:
        schema = 'games'
        table = 'franchise'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Franchise(id={self.id}, name={self.name}"
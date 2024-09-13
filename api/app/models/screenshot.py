from tortoise import fields

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class Screenshot(BaseModel):
    id = fields.IntField(pk=True)
    game = fields.ForeignKeyField('Game', related_name='franchises')
    height = fields.IntField()
    image_id = fields.CharField()
    url = fields.CharField()
    width = fields.IntField()
    alpha_channel = fields.BooleanField()
    animated = fields.BooleanField()
    
    
    class Meta:
        schema = 'games'
        table = 'screenshot'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
    
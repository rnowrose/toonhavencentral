from tortoise import fields

from api.app.const import WebsiteCategory
from api.app.models.base_model import BaseModel

class GameWebsite(BaseModel):
    id = fields.IntField(pk=True)
    trusted = fields.BooleanField()
    url = fields.CharField()
    game = fields.ForeignKeyField('Game', related_name='franchises')
    category = fields.CharField(max_length=10, choices=WebsiteCategory.Choice)
    

    
    class Meta:
        schema = 'games'
        table = 'game_website'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
from app.const import WebsiteCategory
from app.models.base_model import BaseModel
from django.db.models import *


class GameWebsite(BaseModel):
    trusted = BooleanField()
    url = CharField()
    game = ForeignKey('Game', related_name='franchises')
    category = CharField(max_length=10, choices=WebsiteCategory.Choice)
    

    
    class Meta:
        db_table = 'game_website'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
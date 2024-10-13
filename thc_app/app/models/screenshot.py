from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class Screenshot(BaseModel):
    game = ForeignKey('Game', related_name='screenshots')
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()
    
    
    class Meta:
        db_table = 'screenshot'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
    
from django.db.models import *

from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class Screenshot(BaseModel):
    id = IntegerField(pk=True)
    game = ForeignKey('Game', related_name='screenshots')
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()
    
    
    class Meta:
        schema = 'games'
        table = 'screenshot'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
    
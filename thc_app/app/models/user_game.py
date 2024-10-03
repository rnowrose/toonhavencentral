from django.db.models import *

from api.app.const import UserGameStatus
from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class UserGame(BaseModel):
    id = IntegerField(pk=True)
    game = ForeignKey('Game', related_name='games')
    user = ForeignKey('User', related_name='franchises')
    status = CharField(choices=UserGameStatus.Choice)
    
    class Meta:
        schema = 'games'
        table = 'user_game'
        table_description = 'Game Interaction with users'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
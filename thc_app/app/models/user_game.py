from app.const import UserGameStatus
from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class UserGame(BaseModel):
        game = ForeignKey('Game', related_name='games')
    user = ForeignKey('User', related_name='franchises')
    status = CharField(choices=UserGameStatus.Choice)
    
    class Meta:
        db_table = 'user_game'
        table_description = 'Game Interaction with users'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
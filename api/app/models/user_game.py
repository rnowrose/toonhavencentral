from tortoise.models import Model
from tortoise import fields

from api.app.const import UserGameStatus
from api.app.models.base_model import BaseModel
from api.app.models.games import Game


class UserGame(BaseModel):
    id = fields.IntField(pk=True)
    game = fields.ForeignKeyField('Game', related_name='games')
    user = fields.ForeignKeyField('User', related_name='franchises')
    status = fields.CharField(choices=UserGameStatus.Choice)
    
    class Meta:
        schema = 'games'
        table = 'user_game'
        table_description = 'Game Interaction with users'    
    

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
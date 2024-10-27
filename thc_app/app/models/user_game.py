from app.const import UserGameStatus
from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class UserGame(BaseModel):
    game_id = SmallIntegerField()
    user_profile = ForeignKey("UserProfile", related_name="users")
    status = CharField(choices=UserGameStatus.Choice)

    class Meta:
        db_table = "user_game"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

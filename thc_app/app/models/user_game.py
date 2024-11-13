from app.const import UserGameStatus
from app.models.base_model import BaseModel
from django.db.models import *


class UserGame(BaseModel):
    game = ForeignKey("Game", on_delete=CASCADE, related_name="user_games", null=True)
    user_profile = ForeignKey("UserProfile", related_name="user_games", on_delete=CASCADE)
    status = SmallIntegerField(choices=UserGameStatus.Choices)

    class Meta:
        db_table = 'user_game'

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

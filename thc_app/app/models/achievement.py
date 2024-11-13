from app.models.base_model import BaseModel
from app.models.games import Game
from app.models.user_profile import UserProfile
from django.db.models import *


class Achievement(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="achievements")
    game = ForeignKey(
        Game, on_delete=CASCADE, related_name="achievements", null=True
    )
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    date_achieved = DateTimeField()

    class Meta:
        db_table = "achievement"

    def __str__(self):
        return f"{self.title} - {self.user.username}"

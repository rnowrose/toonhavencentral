from app.const import WebsiteCategory
from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class GameWebsite(BaseModel):
    trusted = BooleanField()
    url = CharField()
    game = ForeignKey(Game, on_delete=CASCADE, related_name="game_web")
    category = CharField(max_length=10, choices=WebsiteCategory.Choices)

    class Meta:
        db_table = "game_website"

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"

from app.models.base_model import BaseModel
from django.db.models import *


class GameVideo(BaseModel):
    name = CharField(max_length=200)
    video_id = CharField(max_length=200)
    game = ForeignKey("Game", on_delete=CASCADE, related_name="videos")

    class Meta:
        db_table = "game_video"

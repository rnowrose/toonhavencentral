from app.const import Region, ReleaseDateCategory
from app.models.base_model import BaseModel
from app.models.games import Game
from app.models.platform import Platform
from django.db.models import *


class ReleaseDate(BaseModel):
    game = ForeignKey(Game, on_delete=CASCADE, related_name="release_dates")
    platform = ForeignKey(Platform, on_delete=CASCADE, related_name="platforms")
    category = SmallIntegerField(choices=ReleaseDateCategory.Choices)
    date = DateTimeField()
    human = CharField(max_length=255)
    m = SmallIntegerField()
    region = SmallIntegerField(choices=Region.Choices)
    status = ForeignKey(Game, on_delete=CASCADE, related_name="release_date_status")
    y = SmallIntegerField()

    class Meta:
        db_table = "release_date"

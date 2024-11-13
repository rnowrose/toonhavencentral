from app.const import GameCategory, Status
from app.models.base_model import BaseModel
from app.models.cover import Cover
from app.models.franchise import Franchise
from app.models.player_perspectives import PlayerPerspectives
from django.db.models import *


class Game(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=128)
    url = CharField(max_length=128)
    summary = TextField()
    storyline = TextField()
    collections = JSONField()
    franchise = ForeignKey(Franchise, on_delete=CASCADE, related_name="franchises")
    franchises = JSONField()
    aggregated_rating = DecimalField(max_digits=6, decimal_places=2)
    aggregated_rating_count = IntegerField()
    bundles = JSONField()
    status = CharField(max_length=10, choices=Status.Choices)
    category = CharField(max_length=10, choices=GameCategory.Choices)
    cover = ForeignKey(Cover, on_delete=CASCADE, related_name="cover")
    dlcs = JSONField()
    hypes = IntegerField()
    ports = JSONField()
    rating = DecimalField(max_digits=6, decimal_places=2)
    rating_count = IntegerField()
    remakes = JSONField()
    remasters = JSONField()
    similar_games = JSONField()
    standalone_expansions = JSONField()
    version_parent = ForeignKey("Game", on_delete=CASCADE, related_name="parent_game")
    total_rating = DecimalField(max_digits=6, decimal_places=2)
    total_rating_count = IntegerField()
    platforms = JSONField()
    screenshots = JSONField()
    player_perspectives = ForeignKey(
        PlayerPerspectives, on_delete=CASCADE, related_name="player_perspectives"
    )
    genres = JSONField(default=list)
    websites = JSONField(default=list)
    alternative_names = JSONField(default=list)
    expanded_games = JSONField(default=list)

    class Meta:
        db_table = "game"

    def __repr__(self):
        return f"Game(id={self.id}, name={self.name}"

from app.const import GameCategory, Status
from app.models.base_model import BaseModel
from app.models.cover import Cover
from app.models.franchise import Franchise
from app.models.platform import Platform
from app.models.player_perspectives import PlayerPerspectives
from django.db.models import *


class Game(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=128)
    url = CharField(max_length=128)
    summary = TextField(blank=True, null=True)
    storyline = TextField(blank=True, null=True)
    collections = JSONField(default=list)
    franchise = ForeignKey(Franchise, on_delete=CASCADE, related_name="franchises", null=True)
    franchises = JSONField(default=list)
    aggregated_rating = DecimalField(max_digits=6, decimal_places=2, default=0)
    aggregated_rating_count = IntegerField(default=0)
    bundles = JSONField(default=list)
    status = CharField(max_length=10, choices=Status.Choices)
    category = CharField(max_length=10, choices=GameCategory.Choices)
    cover = ForeignKey(Cover, on_delete=CASCADE, related_name="cover", null=True)
    dlcs = JSONField(default=list)
    hypes = IntegerField(default=0)
    ports = JSONField(default=list)
    rating = DecimalField(max_digits=6, decimal_places=2, default=0)
    rating_count = IntegerField(default=0)
    remakes = JSONField(default=list)
    remasters = JSONField(default=list)
    similar_games = JSONField(default=list)
    standalone_expansions = JSONField(default=list)
    version_parent = ForeignKey(
        "Game", on_delete=CASCADE, related_name="parent_game", null=True
    )
    total_rating = DecimalField(max_digits=6, decimal_places=2, default=0)
    total_rating_count = IntegerField(default=0)
    platforms = JSONField(default=list)
    player_perspectives = ForeignKey(
        PlayerPerspectives,
        on_delete=CASCADE,
        related_name="player_perspectives",
        null=True,
    )
    genres = JSONField(default=list)
    alternative_names = JSONField(default=list)
    expanded_games = JSONField(default=list)

    class Meta:
        db_table = "game"

    def __repr__(self):
        return f"Game(id={self.id}, name={self.name}"

    @property
    def platforms(self):
        console = []
        for platform in self.platforms:
            console.append(Platform.objects.get(platform))
        return console

    @property
    def get_released_games(self):
        return Game.objects.filter(status=Status.RELEASED)

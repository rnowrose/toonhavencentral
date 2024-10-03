from app.const import GameCategory, Status
from app.models.base_model import BaseModel
from django.db.models import *


class Game(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    slug = CharField(max_length=128)
    url = CharField(max_length=128)
    summary = TextField()
    storyline = TextField()
    collection = ForeignKey('Collection', related_name='collections')
    collections = JSONField()
    bundles = JSONField()
    franchise = ForeignKey('Franchise', related_name='franchises')
    franchises = JSONField()
    bundles = JSONField()
    aggregated_rating = DecimalField(decimal_places=2)
    aggregated_rating_count = IntegerField()
    bundles = JSONField()
    status = CharField(max_length=10, choices=Status.Choices)
    category = CharField(max_length=10, choices=GameCategory.Choices)
    cover = ForeignKey('Cover', related_name='cover')
    dlcs = JSONField()
    hypes = IntegerField()
    ports = JSONField()
    rating = DecimalField(decimal_places=2)
    rating_count = IntegerField()
    remakes = JSONField()
    remaster = JSONField()
    similar_games = JSONField()
    standalone_expansions = JSONField()
    version_parent = ForeignKey('Game', related_name='parent_game')
    total_rating = DecimalField(decimal_places=2)
    total_rating_count = IntegerField()

    class Meta:
        schema = 'games'
        table = 'game'
        table_description = 'Video Games!'    
    

    def __repr__(self):
        return f"Game(id={self.id}, name={self.name}"
from tortoise import fields

from api.app.const import GameCategory, Status
from api.app.models.base_model import BaseModel


class Game(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=128)
    url = fields.CharField(max_length=128)
    summary = fields.TextField()
    storyline = fields.TextField()
    collection = fields.ForeignKeyField('Collection', related_name='collections')
    collections = fields.JSONField()
    bundles = fields.JSONField()
    franchise = fields.ForeignKeyField('Franchise', related_name='franchises')
    franchises = fields.JSONField()
    bundles = fields.JSONField()
    aggregated_rating = fields.DecimalField(decimal_places=2)
    aggregated_rating_count = fields.IntField()
    bundles = fields.JSONField()
    status = fields.CharField(max_length=10, choices=Status.Choices)
    category = fields.CharField(max_length=10, choices=GameCategory.Choices)
    cover = fields.ForeignKeyField('Cover', related_name='cover')
    dlcs = fields.JSONField()
    hypes = fields.IntField()
    ports = fields.JSONField()
    rating = fields.DecimalField(decimal_places=2)
    rating_count = fields.IntField()
    remakes = fields.JSONField()
    remaster = fields.JSONField()
    similar_games = fields.JSONField()
    standalone_expansions = fields.JSONField()
    version_parent = fields.ForeignKeyField('Game', related_name='parent_game')
    total_rating = fields.DecimalField(decimal_places=2)
    total_rating_count = fields.IntField()

    class Meta:
        schema = 'games'
        table = 'game'
        table_description = 'Video Games!'    
    

    def __repr__(self):
        return f"Game(id={self.id}, name={self.name}"
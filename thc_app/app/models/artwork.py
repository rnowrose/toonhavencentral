from app.models.base_model import BaseModel
from django.db.models import *


class Artwork(BaseModel):
    game = ForeignKey('Game', related_name='artworks', on_delete=CASCADE)
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()
    
    class Meta:
        db_table = "artwork"

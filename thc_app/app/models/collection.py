from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class Collection(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=255)
    type = ForeignKey("CollectionType", related_name="collection_types")
    url = CharField(max_length=255)

    class Meta:
        db_table = "collection"
        table_description = "Game Data"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class CollectionMembership(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=255)
    collection = ForeignKey("Collection", related_name="collections")
    game = ForeignKey("Game", related_name="game")
    type = ForeignKey(
        "CollectionMembershipType", related_name="collection_membership_type"
    )
    url = CharField(max_length=255)

    class Meta:
        db_table = "collection"
        table_description = "Game Data"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

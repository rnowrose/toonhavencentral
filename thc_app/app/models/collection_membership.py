from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class CollectionMembership(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=255)
    collection = ForeignKey("Collection", related_name="collections", on_delete=CASCADE)
    game = ForeignKey("Game", related_name="game", on_delete=CASCADE)
    type = ForeignKey(
        "CollectionMembershipType",
        related_name="collection_membership_type",
        on_delete=CASCADE,
    )
    url = CharField(max_length=255)

    class Meta:
        db_table = "collection_memebership"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

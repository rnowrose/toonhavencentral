from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class CollectionMembershipType(BaseModel):
    name = CharField(max_length=255)
    description = TextField()
    allowed_collection_type = ForeignKey(
        "CollectionType", on_delete=CASCADE, related_name="allowed_collection_types"
    )

    class Meta:
        db_table = "collection_membership_type"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

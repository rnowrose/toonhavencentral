from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class CollectionRelationType(BaseModel):
    name = CharField(max_length=255)
    description = TextField()
    allowed_child_type = ForeignKey(
        "CollectionType", related_name="parent_collection_types", on_delete=CASCADE
    )
    allowed_parent_type = ForeignKey(
        "CollectionType", related_name="child_collection_types", on_delete=CASCADE
    )

    class Meta:
        db_table = "collection_relation_type"

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"

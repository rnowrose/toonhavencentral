from app.models.base_model import BaseModel
from django.db.models import *


class Keyword(BaseModel):
    name = CharField()
    slug = CharField()
    url = CharField()
    game = ForeignKey("Game", related_name="keywords")

    class Meta:
        db_table = "keyword"

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"

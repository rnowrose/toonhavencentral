from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class Franchise(BaseModel):
    name = CharField(max_length=100)
    slug = CharField(max_length=100)
    url = CharField(max_length=100)

    class Meta:
        db_table = "franchise"

    def __repr__(self):
        return f"Franchise(id={self.id}, name={self.name}"

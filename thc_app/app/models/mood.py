from app.models.base_model import BaseModel
from django.db.models import *


class Mood(BaseModel):
    name = CharField(max_length=50)

    class Meta:
        db_table = "mood"
        table_description = "A list of video game franchises such as Star Wars"

    def __repr__(self):
        return f"Mood(id={self.id}, name={self.name}"

from app.models.base_model import BaseModel
from django.db.models import *


class Theme(BaseModel):
    name = CharField(max_length=255)
    slug = CharField(max_length=255)
    url = CharField(max_length=255)

    class Meta:
        db_table = "theme"

    def __repr__(self):
        return f"Theme(id={self.id}, name={self.name}"

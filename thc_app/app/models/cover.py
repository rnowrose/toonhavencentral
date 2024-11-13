from app.models.base_model import BaseModel
from django.db.models import *


class Cover(BaseModel):
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()

    class Meta:
        db_table = 'cover'

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"

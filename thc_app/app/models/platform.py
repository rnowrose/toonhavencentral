from app.const import PlatformCategory
from app.models.base_model import BaseModel
from django.db.models import *


class Platform(BaseModel):
    name = CharField(max_length=255)
    abbreviation = CharField(max_length=255)
    alternative_name = CharField(max_length=255)
    category = SmallIntegerField(
        default=PlatformCategory.NONE, choices=PlatformCategory.Choices
    )
    generation = IntegerField()
    slug = CharField(max_length=255)
    summary = TextField()
    url = CharField(max_length=255)

    class Meta:
        db_table = 'platform'

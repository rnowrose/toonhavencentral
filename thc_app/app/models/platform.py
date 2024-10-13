from app.const import Platforms
from app.models.base_model import BaseModel
from django.db.models import *


class Platform(BaseModel):
    name = CharField(max_length=255)
    abbreviation = CharField(max_length=255)
    alternative_name = CharField(max_length=255)
    category = CharField(max_length=10, choices=Platforms.Choices)
    generation = IntegerField()
    slug = CharField()
    summary = TextField()
    url = CharField()

    
    class Meta:
        db_table = 'platform'
        table_description = 'a list of all the video game systems'    
    
    

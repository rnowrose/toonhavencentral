from app.const import PlatformEnum
from app.models.base_model import BaseModel
from django.db.models import *


class PlatformFamily(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    slug = CharField()

    class Meta:
        schema = 'games'
        table = 'platform_family'
        table_description = 'a list of all the video game systems'    
    
    

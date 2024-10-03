from django.db.models import *

from api.app.const import PlatformEnum
from api.app.models.base_model import BaseModel


class PlatformFamily(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=255)
    slug = CharField()

    class Meta:
        schema = 'games'
        table = 'platform_family'
        table_description = 'a list of all the video game systems'    
    
    

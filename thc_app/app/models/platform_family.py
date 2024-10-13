from app.const import PlatformEnum
from app.models.base_model import BaseModel
from django.db.models import *


class PlatformFamily(BaseModel):
    name = CharField(max_length=255)
    slug = CharField()

    class Meta:
        db_table = 'platform_family'
        table_description = 'a list of all the video game systems'    
    
    

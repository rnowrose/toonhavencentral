from app.models.base_model import BaseModel
from django.db.models import *


class PlatformLogo(BaseModel):
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()
    
    class Meta:
        db_table = 'platform_logo'
        table_description = 'game system logo images'    
    
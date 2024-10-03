from app.models.base_model import BaseModel
from django.db.models import *


class PlatformLogo(BaseModel):
    id = IntegerField(pk=True)
    height = IntegerField()
    image_id = CharField()
    url = CharField()
    width = IntegerField()
    alpha_channel = BooleanField()
    animated = BooleanField()
    
    class Meta:
        schema = 'games'
        table = 'platform_logo'
        table_description = 'game system logo images'    
    
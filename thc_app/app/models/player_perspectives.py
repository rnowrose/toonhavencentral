from app.models.base_model import BaseModel
from django.db.models import *

class PlayerPerspectives(BaseModel):
    name = CharField(max_length=200)
    slug = CharField(max_length=200)
    url = CharField(max_length=200)
    
    class Meta: 
        db_table = 'player_perspectives'

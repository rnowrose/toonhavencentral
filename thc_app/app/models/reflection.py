from app.models.base_model import BaseModel
from django.db.models import *


class Reflection(BaseModel):
    id = IntegerField(pk=True)
    user = ForeignKey('User', related_name='reflections')
    date = DateTimeField(auto_now_add=True)
    reflection_text = TextField()
    
    class Meta:
        schema = 'games'
        table = 'reflection'
        table_description = 'A list of video game franchises such as Star Wars'    
    
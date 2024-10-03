from django.db.models import *
, models

from app.models.base_model import BaseModel


class Mood(BaseModel):
    id = IntegerField(pk=True)
    name = CharField(max_length=50)

    
    class Meta:
        schema = 'games'
        table = 'mood'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Mood(id={self.id}, name={self.name}"
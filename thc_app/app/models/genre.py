from app.models.base_model import BaseModel
from django.db.models import *


class Genre(BaseModel):
    id = IntegerField(pk=True)
    name = CharField()
    slug = CharField()
    url = CharField()
    
    class Meta:
        schema = 'games'
        table = 'genre'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
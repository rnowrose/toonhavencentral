from app.models.base_model import BaseModel
from django.db.models import *


class Keyword(BaseModel):
    id = IntegerField(pk=True)
    name = CharField()
    slug = CharField()
    url = CharField()
    game = ForeignKey('Game', related_name='screenshots')

    
    class Meta:
        schema = 'games'
        table = 'keyword'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
from django.db.models import *

from api.app.const import PlatformWebsite
from api.app.models.base_model import BaseModel


class PlatformWebsite(BaseModel):
    id = IntegerField(pk=True)
    trusted = BooleanField()
    url = CharField()
    category = CharField(max_length=10, choices=PlatformWebsite.Choice)
    

    
    class Meta:
        schema = 'games'
        table = 'platform_website'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
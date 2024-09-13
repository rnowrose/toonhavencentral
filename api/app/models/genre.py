from tortoise import fields

from api.app.models.base_model import BaseModel

class Genre(BaseModel):
    id = fields.IntField(pk=True)
    name = fields.CharField()
    slug = fields.CharField()
    url = fields.CharField()
    
    class Meta:
        schema = 'games'
        table = 'genre'
        table_description = 'A list of video game franchises such as Star Wars'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
from app.models.base_model import BaseModel
from app.models.games import Game
from django.db.models import *


class GamingSession(BaseModel):
    game = ForeignKey("Game", related_name="sessions")
    user = ForeignKey('User', related_name='sessions')
    session_start = DateTimeField()
    session_end = DateTimeField()
    playtime = FloatField()  # in hours
    progress = TextField(null=True)
    notes = TextField(null=True)
    mood = ForeignKey("Mood", related_name="sessions", null=True)
    
    
    class Meta:
        db_table = 'gaming_session'
        table_description = 'Keeps Track of User info'    
    

    def __repr__(self):
        return f"Genre(id={self.id}, name={self.name}"
    
from app.models.base_model import BaseModel
from app.models.gaming_session import GamingSession
from app.models.user_profile import UserProfile
from django.db.models import *


class Mood(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="moods")
    session = ForeignKey(GamingSession, on_delete=CASCADE, null=True, blank=True)
    game_id = IntegerField()
    mood_before = CharField(max_length=50)
    mood_after = CharField(max_length=50)
    custom_mood = CharField(max_length=50, null=True, blank=True)
    date_logged = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mood'

    def __repr__(self):
        return f"Mood(id={self.id}, name={self.name}"

    def __str__(self):
        return f"Mood for {self.user.username} - {self.game.name if self.game else 'General'}"

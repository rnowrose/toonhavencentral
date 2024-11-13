from app.models.base_model import BaseModel
from app.models.games import Game
from app.models.user_profile import UserProfile
from django.db.models import *


class GamingSession(BaseModel):
    user = ForeignKey(
        UserProfile, on_delete=CASCADE, related_name="user_gaming_sessions"
    )
    game = ForeignKey(
        Game, on_delete=CASCADE, related_name="game_gaming_sessions", null=True
    )
    start_time = DateTimeField()
    end_time = DateTimeField()
    duration = DurationField(null=True, blank=True)
    level = CharField(max_length=100, null=True, blank=True)
    notable_events = TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time
        super().save(*args, **kwargs)

    class Meta:
        db_table = "gaming_session"

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.start_time.date()}"

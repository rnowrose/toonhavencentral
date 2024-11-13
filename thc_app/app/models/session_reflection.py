from app.models.base_model import BaseModel
from app.models.gaming_session import GamingSession
from django.db.models import *


class SessionReflection(BaseModel):
    session = OneToOneField(GamingSession, on_delete=CASCADE, related_name="session_reflections")
    strategies = TextField(null=True, blank=True)
    emotional_response = TextField(null=True, blank=True)
    additional_notes = TextField(null=True, blank=True)

    class Meta:
        db_table = 'session_reflection'

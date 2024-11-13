from app.models.base_model import BaseModel
from app.models.gaming_session import GamingSession
from django.db.models import *


class ReleaseDateStatus(BaseModel):
    name = CharField(max_length=255)
    description = TextField()

    class Meta:
        db_table = "release_date_status"

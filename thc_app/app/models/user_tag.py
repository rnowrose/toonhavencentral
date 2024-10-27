from django.db.models import *

from thc_app.app.models.base_model import BaseModel
from thc_app.app.models.gaming_session import GamingSession
from thc_app.app.models.user_profile import UserProfile


class UserTag(BaseModel):
    name = CharField(max_length=50)
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="tags")
    sessions = ManyToManyField(GamingSession, related_name="tags", blank=True)

    class Meta:
        db_table = "user_tag"

    def __str__(self):
        return self.name

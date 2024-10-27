from thc_app.app.models.base_model import BaseModel
from django.db.models import *

from thc_app.app.models.user_profile import UserProfile

class Achievement(BaseModel):
    user = ForeignKey(
        UserProfile, on_delete=CASCADE, related_name="achievements"
    )
    game_id = IntegerField()
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    date_achieved = DateTimeField()
    
    class Meta:
        db_table='achievement'

    def __str__(self):
        return f"{self.title} - {self.user.username}"

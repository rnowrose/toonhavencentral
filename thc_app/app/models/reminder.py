from thc_app.app.models.base_model import BaseModel
from thc_app.app.models.custom_goal import CustomGoal
from thc_app.app.models.user_profile import UserProfile

from django.db.models import *

class Reminder(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="moods")
    goal = ForeignKey(
        CustomGoal, on_delete=CASCADE, null=True, blank=True
    )
    description = CharField(max_length=255)
    remind_at = DateTimeField()
    is_active = BooleanField(default=True)
    
    class Meta:
        db_table = 'reminder'

    def __str__(self):
        return f"Reminder for {self.user.username}: {self.description}"

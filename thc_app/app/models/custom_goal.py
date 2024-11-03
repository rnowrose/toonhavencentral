from app.models.base_model import BaseModel
from app.models.user_profile import UserProfile
from django.db.models import *


class CustomGoal(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="custom_goals")
    game_id = IntegerField()
    goal_description = CharField(max_length=255)
    is_completed = BooleanField(default=False)
    target_date = DateField(null=True, blank=True)
    completion_date = DateField(null=True, blank=True)

    class Meta:
        db_table = 'custom_goal'

    def __str__(self):
        return f"Goal: {self.goal_description} - {self.user.username}"

from app.models.base_model import BaseModel
from app.models.user_profile import UserProfile
from django.db.models import *


class InsightReport(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="insight_reports")
    generated_on = DateField(auto_now_add=True)
    most_played_game_id = IntegerField()
    average_session_length = DurationField()
    total_playtime = DurationField()
    mood_trend_analysis = TextField(null=True, blank=True)

    class Meta:
        db_table = 'insight_report'

from django.db.models import *

from thc_app.app.models.base_model import BaseModel
from thc_app.app.models.user_profile import UserProfile


class InsightReport(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="insight_reports")
    generated_on = DateField(auto_now_add=True)
    most_played_game_id = IntegerField(
        null=True, blank=True, related_name="most_played_in_reports"
    )
    average_session_length = DurationField()
    total_playtime = DurationField()
    mood_trend_analysis = TextField(null=True, blank=True)

from thc_app.app.models.base_model import BaseModel
from thc_app.app.models.user_profile import UserProfile
from django.db.models import *


class DataExport(BaseModel):
    user = ForeignKey(
        UserProfile, on_delete=CASCADE, related_name="data_exports"
    )
    exported_at = DateTimeField(auto_now_add=True)
    file_type = CharField(
        max_length=10, choices=[("PDF", "PDF"), ("CSV", "CSV")]
    )

    def __str__(self):
        return f"Data Export - {self.user.username} - {self.exported_at}"

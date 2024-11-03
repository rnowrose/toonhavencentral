from app.models.base_model import BaseModel
from app.models.user_profile import UserProfile
from django.db.models import *


class DataExport(BaseModel):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name="data_exports")
    exported_at = DateTimeField(auto_now_add=True)
    file_type = CharField(max_length=10, choices=[("PDF", "PDF"), ("CSV", "CSV")])
    
    class Meta:
        db_table = 'data_export'

    def __str__(self):
        return f"Data Export - {self.user.username} - {self.exported_at}"

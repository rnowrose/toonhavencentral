from app.models.base_model import BaseModel
from django.db.models import *


class Reflection(BaseModel):
    user_id = SmallIntegerField()
    date = DateTimeField(auto_now_add=True)
    reflection_text = TextField()

    class Meta:
        db_table = "reflection"

from app.models.base_model import BaseModel
from django.db.models import *
from django.contrib.auth.models import User


class UserProfile(BaseModel, User):
    profile_name = CharField(unique=True)
    profile_picture = CharField()
    bio = TextField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    login_token = CharField(max_length=50)
    oauth_provider = CharField(max_length=50, null=True)
    oauth_id = CharField(max_length=128, unique=True, null=True)

    class Meta:
        db_table = "user_profile"

    def __repr__(self):
        return f"User(cid={self.user_id}, name={self.profile_name})"

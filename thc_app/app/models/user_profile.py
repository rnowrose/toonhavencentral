from app.models.base_model import BaseModel
from django.db.models import *
from django.contrib.auth.models import User

from app.models.user_game import UserGame


class UserProfile(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="users", null=True)
    profile_name = CharField(max_length=255, unique=True)
    profile_picture = CharField(max_length=255, null=True)
    bio = TextField(null=True)
    login_token = CharField(max_length=50, null=True)
    oauth_provider = CharField(max_length=50, null=True)
    oauth_id = CharField(max_length=128, unique=True, null=True)

    class Meta:
        db_table = 'user_profile'

    def __repr__(self):
        return f"User(cid={self.user_id}, name={self.profile_name})"

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def email(self):
        return self.user.username

    @property
    def user_games(self):
        games = []
        users = UserGame.objects.filter(user_profile=self)
        for user in users:
            games.extend(user.game)
        return games

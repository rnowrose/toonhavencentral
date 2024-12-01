from app.dto.user import NewUser
from django.contrib.auth.models import User
from django.db import transaction

from app.models.user_profile import UserProfile
from app.exceptions import UserAlreadyExists


def create_user(user: NewUser):
    if User.objects.filter(username=user.email).exists():
        raise UserAlreadyExists(user.email)
    
    with transaction.atomic():
        new_user = User.objects.create_user(first_name=user.first_name, last_name=user.last_name, username=user.username, password=user.password)
        
        UserProfile.objects.create(
            user=new_user,
            bio=user.bio,
            profile_name=user.profile_name,
            profile_picture=user.profile_picture,
        )
    return user

def user_info(user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.filter(user=user)
    
    return 
    
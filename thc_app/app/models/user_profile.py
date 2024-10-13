from app.models.base_model import BaseModel
from django.db.models import *


class UserProfile(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True, related_name='customer')
    email = CharField(unique=True)
    password = CharField()
    profile_name = CharField(unique=True)
    profile_picture = CharField()
    first_name = CharField()
    last_name = CharField()
    bio = TextField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    login_token = CharField()
    oauth_provider = CharField(max_length=50, null=True)
    oauth_id = CharField(max_length=128, unique=True, null=True)
    
    
    class Meta:
        db_table = 'user'
        table_description = 'All User Information'

    #products: Mapped[list["Product"]] = relationship(back_populates="category")
    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
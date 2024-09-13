from tortoise.models import Model
from tortoise import fields

from api.app.models.base_model import BaseModel


class User(BaseModel):
    id = fields.IntField(pk=True)
    email = fields.TextField(unique=True)
    password = fields.TextField()
    profile_name = fields.TextField(unique=True)
    profile_picture = fields.TextField()
    first_name = fields.TextField()
    last_name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    login_token = fields.TextField()
    oauth_provider = fields.CharField(max_length=50, null=True)
    oauth_id = fields.CharField(max_length=128, unique=True, null=True)
    
    
    class Meta:
        schema = 'games'
        table = 'user'
        table_description = 'All User Information'

    #products: Mapped[list["Product"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"User(cid={self.id}, name={self.profile}, email={self.email})"
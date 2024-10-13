from app.models.base_model import BaseModel
from django.db.models import *


class PersonalGoal(BaseModel):
    user = ForeignKey('models.User', related_name='goals')
    description = CharField(max_length=250)
    is_completed = BooleanField(default=False)
    target_date = DateTimeField(null=True)
    
    class Meta:
        db_table = 'personal_goal'
        table_description = 'A list of video game franchises such as Star Wars'    
    
from django.db.models import *

from api.app.models.base_model import BaseModel


class PersonalGoal(BaseModel):
    id = IntegerField(pk=True)
    user = ForeignKey('models.User', related_name='goals')
    description = CharField(max_length=250)
    is_completed = BooleanField(default=False)
    target_date = DateTimeField(null=True)
    
    class Meta:
        schema = 'games'
        table = 'personal_goal'
        table_description = 'A list of video game franchises such as Star Wars'    
    
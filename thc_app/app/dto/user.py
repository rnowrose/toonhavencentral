from ninja import Schema


class UserLogin(Schema):
    username: str
    password: str
    
class TokenSchema(Schema):
    refresh: str
    access: str

class NewUser(Schema): 
    first_name: str
    last_name: str
    email: str
    password: str
    profile_name: str
    bio: str
    profile_picture: str
    
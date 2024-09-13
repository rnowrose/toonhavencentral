from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class User(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreateNew:
    pass


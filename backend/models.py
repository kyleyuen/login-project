from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class UserInDB(User):
    hashed_password: str

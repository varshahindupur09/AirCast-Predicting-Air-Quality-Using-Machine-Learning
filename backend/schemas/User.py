from pydantic import BaseModel, Field, EmailStr, validator
from typing import Union, List, Optional
from models.User import Role

"""

LoginResponse has four attributes: username, email, access_token, and token_type. 
username and email are of type str, access_token is of type str and token_type is of type str with a default value of "bearer". 
The Config class is used to set orm_mode to True.

"""
class LoginResponse(BaseModel):
    username: str
    email: str
    access_token: str
    token_type: str = "bearer"
    user_type: int = 2

    class Config():
        orm_mode = True


class User(BaseModel):
    username:str = Field(
        default=None,
        title="Please enter valid username",
        min_length=5,
    )
    email: EmailStr
    password:str = Field(
        min_length=5
    )
    planId: int = Field(
        default=1,
        title="Please enter the plan ID (Free - 1, Gold - 2, Platinum - 3)"
        )

    @validator("username", "email", pre=True)
    def lowercase_strings(cls, value):
        if isinstance(value, str):
            return value.lower()
        return value


class TokenData(BaseModel):
    id: int
    email: str
    username: Union[str, None] = None
    userType: int = 2

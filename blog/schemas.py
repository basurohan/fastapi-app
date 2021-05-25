from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str

class BlogExtended(Blog):
    class Config():
        orm_mode = True

class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[BlogExtended] = []

    class Config():
        orm_mode = True

class BlogDTO(BaseModel):
    title: str
    body: str
    user: UserDTO

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
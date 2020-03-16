from typing import List
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    username: str


class UserCreate(UserInfoBase):
    fullname: str
    password: str


class UserAuthenticate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    content: str


class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True








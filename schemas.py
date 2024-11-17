from pydantic import BaseModel, Field


# Authorithation in Bot
class UserCreate(BaseModel):
    username: str
    password: str
    department: str
    position: str


class UserLogin(BaseModel):
    username: str
    password: str


# Message from Users
class From(BaseModel):
    id: int
    is_bot: bool
    first_name: str = None
    username: str = None
    language_code: str


class Chat(BaseModel):
    id: int
    first_name: str
    username: str
    type_chat: str = Field(alias="type")


class Message(BaseModel):
    message_id: int
    fromTg: From = Field(alias="from")
    chat: Chat
    date: int
    text: str


class Answer(BaseModel):
    update_id: int
    message: Message

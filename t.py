from pydantic import BaseModel, Field

d = {
    "update_id": 939319983,
    "message": {
        "message_id": 55,
        "from": {
            "id": 398685944,
            "is_bot": False,
            "first_name": "Melon",
            "username": "qweerty01",
            "language_code": "en",
        },
        "chat": {
            "id": 398685944,
            "first_name": "Melon",
            "username": "qweerty01",
            "type": "private",
        },
        "date": 1731858836,
        "text": "Good",
    },
}


class From(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: str
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

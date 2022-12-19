from pydantic import BaseModel, Field
from datetime import datetime


def get_time():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


class Message(BaseModel):
    recipient: str
    message: str

class TimedMessage(Message):
    date: str = Field(default_factory=get_time)

    class Config:
        orm_mode = True
# src/api_client.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Message(BaseModel):
    username:  str
    content: str


messages: List[Message] = []


@app.post("/send_message/")
def send_message(msg: Message):
    messages.append(msg)
    return {"message": "Mensaje recibido!", "data": msg}


@app.get("/get_messages/")
def get_messages():
    return messages
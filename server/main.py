# from fastapi import FastApi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional

from pydantic import BaseModel

origins = [
    "http://localhost:8080",
    "http://localhost:8081",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    title: str
    sender: str
    content: str
    url: str


@app.get("/")
async def root():
    return FileResponse("dist/index.html")  # StaticFiles(directory="dist")


@app.post("/api/ListMessages/")
async def read_item(simpleVersion: bool):
    global MessagesList
    if not simpleVersion:
        return MessagesList
    simpleList = []
    print(MessagesList)
    for item in MessagesList:
        simpleList.append(
            {
                "title": item["title"],
                "content": item["content"],
                "sender": item["sender"],
            }
        )
    return simpleList


@app.post("/api/CreateMessage/")
async def read_item(message: Message):
    global MessagesList
    MessagesList.append(
        {
            "title": message.title,
            "content": message.content,
            "sender": message.sender,
            "url": message.url,
        }
    )
    return "Got title `%s`, content `%s`, sender `%s` and url `%s`" % (
        message.title,
        message.content,
        message.sender,
        message.url,
    )


MessagesList = [
    {
        "title": "thisis",
        "content": "this is a content",
        "sender": "Tzahi",
        "url": "nothing",
    }
]
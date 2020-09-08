# from fastapi import FastApi
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse

from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("dist/index.html")  # StaticFiles(directory="dist")


@app.post("/ListMessages/")
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


@app.post("/CreateMessage/")
async def read_item(title: str, content: str, sender: str, url: str):
    global MessagesList
    MessagesList.append(
        {
            "title": title,
            "content": content,
            "sender": sender,
            "url": url,
        }
    )
    return "Got title `%s`, content `%s`, sender `%s` and url `%s`" % (
        title,
        content,
        sender,
        url,
    )


MessagesList = [
    {
        "title": "thisis",
        "content": "this is a content",
        "sender": "Tzahi",
        "url": "nothing",
    }
]
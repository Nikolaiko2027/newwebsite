import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


class HelloData(BaseModel):
    name: str


@app.get("/")
def index():
    return FileResponse("index.html")


@app.post("/hello")
def hello(data: HelloData):
    return {"message": f"Привет, {data.name}! Добро пожаловать на мой сайт!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
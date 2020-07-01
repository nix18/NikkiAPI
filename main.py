# api逻辑
from fastapi import FastAPI

from utils import dbUtils

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "又是一个新的闪耀暖暖题库api"}


@app.get("/api/{question}")
async def query(question: str):
    question = question.replace("_", "").replace(" ", "")
    return {"message": dbUtils.outAns(question)}

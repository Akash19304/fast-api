from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends 
from fastapi.responses import HTMLResponse
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_Post": f"title: {payLoad['title']}, content: {payLoad['content']}" }

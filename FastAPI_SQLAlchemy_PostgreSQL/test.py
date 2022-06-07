from typing import Optional
import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int, published: bool, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit } published blogs queried'}
    else:
        return {'data': f'{limit } unpublished blogs queried'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blog list'}


@app.get("/blogs/{id}/comments")
def published_blogs_id(id: int, limit: int = 10):
    return {"data": [f" published blog for id:{id} with {limit} comments"]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return f"Blog is created with title as {blog.title}"

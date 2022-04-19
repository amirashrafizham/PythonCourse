from typing import Optional
from fastapi import FastAPI

app = FastAPI()

"""
STATIC ROUTING (ENDPOINTS WITHOUT ID). YOU HAVE TO PUT THESE ROUTING BEFORE DYNAMIC ONES,
ELSE IT WILL RETURN AN ERROR
"""


@app.get('/blog')
def index(limit: int, published: bool, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs queried'}
    else:
        return {'data': f'{limit} blogs queried'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blog list'}


"""
DYNAMIC ROUTING (ENDPOINTS WITH ID). YOU HAVE TO PUT THESE ROUTING BEFORE DYNAMIC ONES,
ELSE IT WILL RETURN AN ERROR
"""


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/commments')
def comments(id: int, limit: int = 10):
    return {'data': f'{10} comments for id:{id}'}

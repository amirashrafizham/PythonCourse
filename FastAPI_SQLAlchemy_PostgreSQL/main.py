from fastapi import FastAPI, Depends, HTTPException
from config import engine
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestBook
import crud
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return HTTPException(status_code=201, detail="Book created successfully")


@app.get("/")
async def get_books(db: Session = Depends(get_db)):
    _books = crud.get_book(db)
    return _books


@app.patch("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(
        db,
        book_id=request.parameter.id,
        title=request.parameter.title,
        description=request.parameter.description,
    )
    return _book


@app.delete("/delete")
async def delete_book(request: RequestBook, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)
    return HTTPException(status_code=200, detail="Book deleted successfully")

from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: int = Field(description="ID is not needed while creation",default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=5,max_length=100)
    rating: int = Field(gt=0,lt=6 )
    published_date: int = Field(gt=0,lt=9999)

    model_config ={
        "json_schema_extra":{
            "example": {
                        "id": None,
                        "title": "New title",
                        "author": "Sj",
                        "description": "A new book added",
                        "rating": 3,
                        "published_date": 1998
                    }
        }
    }



BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

def find_book_id(book : Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
@app.post("/create_book")
def create_book(book_request : BookRequest):
    book_request =Book(**book_request.dict())
    BOOKS.append(find_book_id(book_request))


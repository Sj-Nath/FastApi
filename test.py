from fastapi import FastAPI,Body

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]
app = FastAPI()

@app.get("/books")
def books():
    return BOOKS

@app.post("/books/create_book")
def create_book(new_book = Body()):
    print(new_book)
    if new_book not in BOOKS:
        print(new_book)
        BOOKS.append(new_book)

@app.put("/books/update_books")
def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
def create_book(book_title :str ):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get("/books/{book_title}")
def books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    else:
        return {"Book Not Found"}
    
@app.get("/books/")
def read_category_by_query(category: str):
    cat_books = []
    for book in BOOKS:
        if book.get("category") == category.casefold():
            cat_books.append(book)
    return cat_books

@app.get("/books/{book_auther}/")
def read_auther_category_by_query(book_auther:str,category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get("author") == book_auther and \
            book.get("category") == category:
            book_to_return.append(book)
    return book_to_return

    
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app=FastAPI()

books=[
    {"title":"Title one","author":"Author one","category":"science"},
    {"title":"Title Two","author":"Author Two","category":"science"},
    {"title":"Title Three","author":"Author Three","category":"history"},
    {"title":"Title Four","author":"Author four","category":"math"},
    {"title":"Title Five","author":"Author Five","category":"math"},
]
# http://127.0.0.1:8000/books/?author=Author Three&category=history
@app.get("/books/")
async def read_by_query(author:str,category:str):
    books_to_return=[]
    for book in books:
        if book.get("author").casefold()==author.casefold() and book.get("category").casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

# URL Request: http://127.0.0.1:8000/books/?category=history
# @app.get("/books/")
# async def read_by_query(category:str):
#     books_to_return=[]
#     for book in books:
#         if book.get("category").casefold()==category.casefold():
#             books_to_return.append(book)
#     return books_to_return
       
# @app.get("/books")
# async def read_books():
#     return books

# @app.get("/books/{dynamic_param}")
# async def read_books(dynamic_param:str):
#     return {'dynamic_param':dynamic_param}
# FastAPI treats "Title one" as a dynamic path parameter, not a title to search for.
# It just returns that string without doing anything with the actual book data.


# @app.get("/books/{title}")
# async def get_book_by_title(title: str):
#     for book in books:
#         if book["title"].lower() == title.lower():
#             return book
#     return JSONResponse(status_code=404, content={"error": "Book not found"})


"""y both at the same time will not work because traffic for the above get method goes completely so sharing of same data/traffic is not possible"""


# @app.get("/books/{category}")
# async def histories(category: str):
#     for cat in books:
#         if cat["category"].lower()==category.lower():
#             return cat
#     return JSONResponse(status_code=404,content={"error" : "not found"})

"""
o/p:
{
  "title": "Title one",
  "author": "Author one",
  "category": "science"
}
"""

# cannot write a separate there might be an conflict occurence
"""
@app.get("/books/Title one")
async def read_all_books():
    return {'book_tile':"My Favourite Book"}
"""
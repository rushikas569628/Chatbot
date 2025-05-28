from fastapi import FastAPI
app=FastAPI()

books=[
    {"title":"Title one","author":"Author one","category":"science"},
    {"title":"Title Two","author":"Author Two","category":"science"},
    {"title":"Title Three","author":"Author Three","category":"history"},
    {"title":"Title Four","author":"Author four","category":"math"},
    {"title":"Title Five","author":"Author Five","category":"math"},
]

@app.get("/books")
async def read_books():
    return books
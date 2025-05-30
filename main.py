from fastapi import FastAPI, Form, Request
from typing import Annotated
from openai import OpenAI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

load_dotenv()
# ✅ Read from Render’s environment variable directly
api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chat_log = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
chat_response = []

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "chat_response": chat_response})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    chat_log.append({'role': 'user', 'content': user_input})
    chat_response.append(f"You: {user_input}")

    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=0
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_response.append(f"Bot: {bot_response}")

    return templates.TemplateResponse("home.html", {"request": request, "chat_response": chat_response})

@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request, "image_url": None})

@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):
    response = openai.images.generate(
        prompt=user_input,
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url

    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})

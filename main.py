from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
openai = OpenAI(api_key=api_key)

# Start the chat log with a system message to define assistant behavior
chat_log = [
    {'role': 'system', 'content': 'You are a helpful assistant.'}
]

# Interactive chat loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "stop":
        print("Conversation ended.")
        break

    # Add user input to the chat log
    chat_log.append({'role': 'user', 'content': user_input})

    # Send the chat log to OpenAI
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=0  # deterministic output
    )

    # Extract assistant response
    bot_response = response.choices[0].message.content

    # Add assistant's reply to the chat log
    chat_log.append({'role': 'assistant', 'content': bot_response})

    # Print assistant's reply
    print("Assistant:", bot_response)

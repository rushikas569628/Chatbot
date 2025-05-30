# 🤖 Personal Chatbot using GPT-3.5 Turbo (FastAPI + OpenAI)

A mini replica of ChatGPT/Gemini built while learning how large language models (LLMs) work. This chatbot can engage in intelligent conversations and generate images from natural language prompts — all deployed via FastAPI.

🔗 **Live Link**: [https://chatbot-7zay.onrender.com](https://chatbot-7zay.onrender.com)

---

## 💡 Technologies Used

- **FastAPI** – For building async web APIs
- **OpenAI GPT-3.5 Turbo** – For conversational AI and image generation
- **Jinja2** – Templating engine for rendering HTML
- **Python Dotenv** – To manage environment variables
- **Render** – For deploying the backend
- **HTML/CSS (Jinja templates)** – For basic UI
- **Uvicorn** – ASGI server for FastAPI

---

## 🎯 Purpose

To understand how large language models work in real-world applications and how to build a full-stack conversational system. This project served as a practical exploration of API communication, LLM behavior, and web deployment.

---

## 🧗 Challenges & Solutions

- ❗ **Limited API usage**:  
  I used the **paid GPT-3.5 API with a $5 credit**. When the quota runs out, users see the message:  
  `"⚠️ The AI is currently unavailable due to usage limits or connection issues"`  
  (Handled via a `try-except` block).

- 🔐 **API Key security**:  
  Learned how `.env` files and `load_dotenv()` help protect sensitive keys.

- 🌐 **Deployment config**:  
  Faced environment setup issues on Render. Solved by using `requirements.txt`, `.env`, and `.render.yaml` correctly.

---

## 📚 Learnings

- 🎛️ **Temperature parameter** in OpenAI:
  - `0` = more deterministic output  
  - `>1` = more creative/random responses  
  - Learned how tweaking `temperature` affects answer style and tone.

- 🔄 **FastAPI bridges the frontend and backend**:
  - It receives user input, talks to OpenAI, and sends back intelligent replies.
  - Simple but powerful for building APIs quickly.

- 🛠️ **Importance of `venv` and `requirements.txt`**:
  - Helps isolate dependencies
  - Makes deployment reproducible
  - Command used:  
    ```bash
    pip freeze > requirements.txt
    ```

---

## ⚙️ Commands Used

```bash
# Activate virtual environment
source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app locally
uvicorn main:app --reload

# Save environment packages
pip freeze > requirements.txt

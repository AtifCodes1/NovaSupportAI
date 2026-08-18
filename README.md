# NovaSupportAI 

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Working-success)
---
An AI-powered customer support agent built with Python, FastAPI, Gemini, and a small REST API backend.

NovaSupportAI can understand customer messages, identify what the customer wants, extract an order number when available, and perform order or return-related actions through backend APIs.

---

## Features

- AI-powered message understanding using Google Gemini
- Conversation-based customer interaction
- Intent detection
- Automatic order number extraction
- Order status checking
- Return eligibility checking
- Return request creation
- Handles missing order numbers by waiting for the customer's next message
- REST API communication using HTTP
- FastAPI application
- Pydantic models for structured data
- Configuration using `config.json`
- Gemini API key loaded through `.env`
- Separate Mock Backend for testing
- Custom API client for backend communication

---

## Project Structure
```text
NovaSupportAI/
│
├── ai/
│   ├── base_ai.py
│   ├── gemini_ai.py
│   ├── models.py
│   └── ...
│
├── api/
│   ├── client.py
│   └── ...
│
├── config/
│   ├── config.json
│   └── config.py
│
├── services/
│   ├── order_service.py
│   ├── return_service.py
│   └── ...
│
├── agent/
│   └── agent.py
│
├── MockBackend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── conversation_manager.py
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
---
## Technologies Used

 Technology     Purpose                               
 
 Python     ___    Main programming language             
 FastAPI    ___   REST API and application server       
 Uvicorn    ___    ASGI server                           
 Google Gemini ___ AI message understanding              
 Pydantic    ___   Data validation and structured models 
 Requests    ___   HTTP communication                    
 python-dotenv ___ Loading environment variables         
 Git & GitHub ___  Version control                       

## 🚀 How Anyone Can Clone and Use This Project

Anyone can clone this repository from GitHub and run NovaSupportAI locally by following the steps below.

### 1. Clone the Repository

First, clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Then move into the project folder:

cd NovaSupportAI

### 2. Create a Virtual Environment

Create a Python virtual environment:

python -m venv .venv

Activate the virtual environment on Windows PowerShell:

.venv\Scripts\Activate.ps1

If you are using Command Prompt instead:

.venv\Scripts\activate

### 3. Install the Required Packages

Install the project's dependencies:

pip install -r requirements.txt

### 4. Set Up the Gemini API Key

NovaSupportAI uses Google Gemini to understand customer messages.

Create a `.env` file in the root directory of the project and add:

GEMINI_API_KEY=your_gemini_api_key_here

Replace `your_gemini_api_key_here` with your own Gemini API key.

Important: Never commit your `.env` file or expose your API key publicly.

### 5. Check the Configuration

The project configuration is stored in:

config/config.json

The default configuration is:

{
    "ai": {
        "provider": "gemini"
    },
    "backend": {
        "url": "http://127.0.0.1:8001"
    }
}

The `backend.url` value tells NovaSupportAI where the backend API is running.

### 6. Set Up the Mock Backend

NovaSupportAI currently uses a separate Mock Backend for development and testing.

Open a new terminal and move into the Mock Backend folder:

cd MockBackend

Create its virtual environment:

python -m venv .venv

Activate it:

.venv\Scripts\Activate.ps1

Install its dependencies:

pip install -r requirements.txt

### 7. Start the Mock Backend

Start the Mock Backend with:

uvicorn main:app --reload --port 8001

The Mock Backend should now be running at:

http://127.0.0.1:8001

You can check it by opening the following address in your browser:

http://127.0.0.1:8001/

You should receive a response showing that the Mock Backend is running.

### 8. Start NovaSupportAI

Open another terminal and go back to the NovaSupportAI project directory.

Activate the NovaSupportAI virtual environment:

.venv\Scripts\Activate.ps1

Then start the FastAPI application:

uvicorn main:app --reload

NovaSupportAI should now be running at:

http://127.0.0.1:8000

### 9. Open the FastAPI Documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

The Swagger UI allows you to test the available API endpoints directly from your browser.

### 10. Send a Chat Request

The main endpoint for interacting with NovaSupportAI is:

POST /chat

Example request:

{
    "user_id": "user123",
    "message": "Where is my order 1001?"
}

You can also try:

{
    "user_id": "user123",
    "message": "Can I return order 1001?"
}

Or:

{
    "user_id": "user123",
    "message": "I want to return order 1001"
}

### 11. Try Different Customer Messages

You can experiment with different messages such as:

Hello

Where is my order 1001?

Can I return order 1001?

I want to return order 1001

Where is my order?

I want to return my order

You can also change the wording of these messages to see how Gemini understands different ways of asking for the same thing.

### 12. Complete Application Flow

The complete NovaSupportAI flow is:
```text
Customer
   ↓
FastAPI /chat
   ↓
ConversationManager
   ↓
Agent
   ↓
Gemini
   ↓
Intent + Action + Order Number
   ↓
OrderService / ReturnService
   ↓
APIClient
   ↓
HTTP GET / POST
   ↓
Mock Backend
   ↓
Response
   ↓
Agent
   ↓
Customer
```
---
### 13. Important Notes

- Python should be installed on your system before running the project.
- The NovaSupportAI and Mock Backend can use separate virtual environments.
- The Mock Backend must be running before testing Order or Return operations.
- NovaSupportAI must also be running to receive customer requests.
- A valid Gemini API key is required.
- Keep your Gemini API key inside `.env`.
- Never commit `.env` to GitHub.
- The current backend is only a Mock Backend used for development and testing.
- The backend URL can be changed through `config/config.json` without changing the service code.

### 14. Final Setup

Once everything is configured, you should have two servers running:

NovaSupportAI:

http://127.0.0.1:8000

Mock Backend:

http://127.0.0.1:8001

Then open:

http://127.0.0.1:8000/docs

and use the `POST /chat` endpoint to interact with NovaSupportAI.

That's all that is required to clone, configure, run, and test the current version of NovaSupportAI locally.

## Author

**Muhammad Atif**

Built with Python, FastAPI, and Gemini.
# Zeeshan AI Chatbot - Backend

FastAPI backend for AI-powered chatbot using Groq API.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

4. Run locally:
```bash
uvicorn main:app --reload
```

5. Visit: http://localhost:8000

## Deployment

Deploy to Railway.app (FREE)
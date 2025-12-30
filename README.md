# Zeeshan Ullah - Portfolio Website with AI Chatbot

A modern, eye-catching portfolio website with an integrated AI-powered chatbot that answers questions about my skills, experience, and projects.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)

## One-Click Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/KhattakDataLab/zeeshan-ai-portfolio)

## Features

- **Modern Dark Theme** - Beautiful gradient animations and glassmorphism effects
- **Fully Responsive** - Works perfectly on desktop, tablet, and mobile
- **AI Chatbot** - Powered by Groq API (LLaMA 3.1) to answer visitor questions
- **Smooth Animations** - Typing effects, scroll reveals, and hover interactions
- **Fast Performance** - Optimized CSS and vanilla JavaScript

## Tech Stack

### Frontend
- HTML5, CSS3 (Custom properties, Flexbox, Grid)
- Vanilla JavaScript (No frameworks)
- Font Awesome Icons
- Google Fonts (Inter, Fira Code)

### Backend
- Python 3.9+
- FastAPI
- Groq API (LLaMA 3.1-8b-instant)
- Uvicorn

## Project Structure

```
zeeshan-ai-portfolio/
├── backend/
│   ├── main.py           # FastAPI server
│   ├── requirements.txt  # Python dependencies
│   └── .env.example      # Environment variables template
├── frontend/
│   ├── index.html        # Main portfolio page
│   ├── styles.css        # Main styles
│   ├── main.js           # Page interactions
│   ├── chatbot-widget.css
│   └── chatbot-widget.js
├── render.yaml           # Render deployment config
└── README.md
```

## Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

Create `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run the server:
```bash
uvicorn main:app --reload
```

### Frontend Setup

Simply open `frontend/index.html` in your browser, or use a local server:
```bash
cd frontend
python -m http.server 3000
```

Visit: http://localhost:3000

## Deployment

### Option 1: One-Click Deploy to Render
1. Click the "Deploy to Render" button above
2. Set `GROQ_API_KEY` environment variable
3. Done!

### Option 2: Manual Deploy

**Backend (Render/Railway):**
1. Create new Web Service
2. Connect GitHub repo
3. Root Directory: `backend`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add `GROQ_API_KEY` environment variable

**Frontend (Render/Vercel/Netlify):**
1. Create new Static Site
2. Connect GitHub repo
3. Root Directory: `frontend`
4. Publish Directory: `./`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| POST | `/api/chat` | Send message to chatbot |
| GET | `/health` | Health check |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key (get free at [console.groq.com](https://console.groq.com)) |

## Author

**Zeeshan Ullah** - GenAI Engineer

- Email: ullahzeeshan202@gmail.com
- LinkedIn: [linkedin.com/in/zeeshanullah](https://linkedin.com/in/zeeshanullah)
- GitHub: [github.com/KhattakDataLab](https://github.com/KhattakDataLab)

## License

MIT License - feel free to use this for your own portfolio!

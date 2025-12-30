from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(title="Zeeshan AI Chatbot API")

# Configure CORS (allow all origins for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Complete Information about Zeeshan from Resume
ZEESHAN_INFO = """
Name: Zeeshan Ullah
Role: GenAI Engineer | RAG Systems | AI Agents | Production LLM Applications
Location: Islamabad, Pakistan
Phone: +92 346 7149800
Email: ullahzeeshan202@gmail.com
LinkedIn: linkedin.com/in/zeeshanullah
GitHub: github.com/KhattakDataLab

PROFESSIONAL SUMMARY:
GenAI Engineer who reduced customer support costs by 40% through RAG-powered chatbots. Built 6 production AI systems processing 10K+ daily queries with 92%+ accuracy. Expert in rapid prototyping: idea to deployed MVP in 48-72 hours. Specialized in LangChain, OpenAI API, and FastAPI deployment. Track record of building bilingual AI solutions (Urdu-English) solving real business problems in Pakistani market.

TECHNICAL SKILLS:
- GenAI & LLMs: LangChain, RAG, OpenAI API, LLaMA 3, Groq API, AI Agents (deployed 6 production systems)
- Vector Databases: Pinecone, ChromaDB, FAISS (managed 50K+ embeddings)
- Backend & APIs: Python, FastAPI, Streamlit, Docker, Git (APIs handling 10K+ requests/day)
- ML/NLP: Scikit-learn, Transformers, Feature Engineering, Model Evaluation
- Cloud & Deployment: Azure ML, CI/CD, Model Monitoring, Production Debugging
- Languages: English (Fluent), Urdu (Native), Pashto (Conversational)

FLAGSHIP PROJECT:
AI-Powered Hiring Assistant | FastAPI, OpenAI Embeddings, Streamlit, PostgreSQL
- Semantic resume-job matching platform serving 500+ users across 3 companies
- Reduced hiring time by 65% (8 hours to 3 hours per candidate screening)
- Built FastAPI backend achieving 92% match accuracy with sub-500ms response time
- Automated resume parsing pipeline processing 100+ resumes/hour
- Live demo: github.com/KhattakDataLab/resume-matcher

PROFESSIONAL EXPERIENCE:

1. AI Engineer | National University of Technology (NUTECH), Islamabad | Jul 2024 – Oct 2024
   - Built customer churn prediction model with 89% accuracy, helping retain $50K+ monthly revenue
   - Automated ML pipelines on Azure reducing data processing time from 6 hours to 2 hours (67% improvement)
   - Deployed FastAPI microservices handling 1000+ daily predictions with 99.9% uptime and sub-500ms latency
   - Collaborated with product team translating business requirements into 5 production-ready ML models

2. Data Science Trainee | Codanics (Remote) | Nov 2023 – Mar 2024
   - Delivered 4 end-to-end ML projects from data collection to deployment achieving 85-92% accuracy
   - Built automated feature engineering pipeline reducing manual work from 4 hours to 30 minutes per dataset
   - Created reusable ML templates adopted by 10+ team members, improving project delivery speed by 40%

3. Data Analyst Intern | Inter-Services Public Relations (ISPR), Islamabad | Jun 2023 – Sep 2023
   - Analyzed 100K+ records identifying 3 key trends that influenced strategic planning decisions
   - Built 10+ interactive Power BI dashboards automating weekly reports and saving 15+ hours per week
   - Streamlined data collection process reducing errors by 35% through automated validation

ADDITIONAL AI PROJECTS:
- AI Email Generator | LLaMA 3, Groq API, Streamlit: Built tone-customizable cold email generator serving 200+ monthly users. Integrated 5 tone variations with 95% user satisfaction rate. Live at: github.com/KhattakDataLab/email-gen
- Smart Crop Recommendation Engine | Scikit-learn, Python: Developed ML model with 88% accuracy helping farmers optimize crop selection. Processed 10K+ agricultural records with automated feature engineering pipeline.

EDUCATION & CERTIFICATIONS:
- Bachelor of Science in Computer Science | CGPA: 3.4/4.0 | Abdul Wali Khan University, Pakistan | 2020-2024
- Associate AI Engineer | NAVTTC & Microsoft Azure | 2024
- AI & Data Science Bootcamp | Codanics | 2024

KEY ACHIEVEMENTS:
- Built 6+ production AI systems
- Handle 10K+ daily queries
- 92%+ accuracy rate
- Reduced customer support costs by 40%
- Idea to MVP in 48-72 hours
- Bilingual solutions (Urdu-English)
"""

# Request model
class ChatRequest(BaseModel):
    message: str

# Response model
class ChatResponse(BaseModel):
    response: str
    success: bool

@app.get("/")
async def root():
    return {
        "message": "Zeeshan AI Chatbot API is running!",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/api/chat (POST)"
        }
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that answers questions about Zeeshan
    """
    try:
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a helpful AI assistant for Zeeshan Ullah's portfolio website. 
                    Answer questions about Zeeshan based on this information: {ZEESHAN_INFO}
                    
                    Guidelines:
                    - Keep answers concise (2-4 sentences)
                    - Be friendly and professional
                    - Use emojis occasionally 😊
                    - If asked something not in the info, politely say you don't have that information
                    - Always encourage visitors to reach out via email or LinkedIn for more details
                    """
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=300,
        )
        
        response_text = chat_completion.choices[0].message.content
        
        return ChatResponse(
            response=response_text,
            success=True
        )
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Sorry, something went wrong. Please try again!"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db, save_assessment
app = FastAPI(title="AI Maturity 360 API")

# CORS (required for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    return {
        "strategy": "Do you have a documented AI strategy aligned with business goals?",
        "data": "Is your data governed, accessible, and ML-ready?",
        "engineering": "Do you have standardized ML pipelines?",
        "governance": "Do you have AI risk, ethics, and compliance processes?",
        "people": "Do teams have AI skills and ownership?"
    }

@app.post("/submit")
def submit_assessment(payload: dict):
    email = payload.get("email")
    answers = payload.get("answers")


    if not email:
        raise HTTPException(status_code=400, detail="Email is required")


    if not answers or not isinstance(answers, dict):
        raise HTTPException(status_code=400, detail="Answers are required")


    total_score = sum(int(v) for v in answers.values())
    max_score = len(answers) * 3
    pct = (total_score / max_score) * 100 if max_score else 0


    if pct <= 20:
        level = "Ad-hoc"
    elif pct <= 40:
        level = "Experimenting"
    elif pct <= 60:
        level = "Operational"
    elif pct <= 80:
        level = "Scaled"
    else:
        level = "Optimized"

    save_assessment(email, total_score, level)

    return {
        "status": "success",
        "email": email,
        "total_score": total_score,
        "maturity_level": level
    }
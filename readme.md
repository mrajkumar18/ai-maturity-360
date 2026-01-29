# ai-maturity-360

**AI Maturity 360** is a full-stack web application that helps individuals and organizations assess their AI maturity across **strategy, data, engineering, governance, and people** dimensions.


<img width="487" height="542" alt="image" src="https://github.com/user-attachments/assets/bc733511-4e3a-422b-be07-8e27ec73d06b" />

It uses a **React frontend**, **FastAPI backend**, and **SQLite** for secure, server-side scoring and persistence.

---

## The project uses

- **React** for the frontend (UI)
- **FastAPI** for the backend (business logic & APIs)
- **SQLite** for persistence (simple, local database)

This architecture intentionally keeps **business rules on the server** and **presentation logic in the browser**.

---

## Why this project exists

Many AI assessments run entirely in the browser, which:

- Exposes scoring logic  
- Allows tampering  
- Cannot safely store results  

This project demonstrates a proper **SaaS-style separation**:

- Frontend collects inputs  
- Backend validates, computes, and stores results  
- Database acts as the system of record  


## Maturity Scoring Model

Each question is scored from **0 to 3**.

| Score % | Maturity Level |
|-------:|----------------|
| 0–20%  | Ad-hoc |
| 21–40% | Experimenting |
| 41–60% | Operational |
| 61–80% | Scaled |
| 81–100% | Optimized |


**All calculations happen server-side.**

## Backend Setup (FastAPI)

### 1. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
2. Install dependencies
pip install fastapi uvicorn
3. Run the backend
uvicorn main:app --reload

Backend will be available at:

http://localhost:8000
Health check
GET /
Frontend Setup (React)
cd frontend
npm install
npm run dev

Frontend will run on:

http://localhost:5173

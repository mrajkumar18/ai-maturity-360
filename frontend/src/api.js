const API_BASE = "http://localhost:8000";

export async function fetchQuestions() {
  const res = await fetch(`${API_BASE}/questions`);
  return res.json();
}

export async function submitAssessment(payload) {
  const res = await fetch("http://localhost:8000/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return res.json();
}
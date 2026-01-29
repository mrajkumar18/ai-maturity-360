import { useEffect, useState } from "react";
import { fetchQuestions, submitAssessment } from "./api";

function App() {
  const [questions, setQuestions] = useState({});
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);

  useEffect(() => {
    fetchQuestions().then(setQuestions);
  }, []);

  const handleChange = (key, value) => {
    setAnswers({ ...answers, [key]: value });
  };

const handleSubmit = async () => {
  if (!email) {
    alert("Email is required");
    return;
  }

  const res = await submitAssessment({
    email,
    answers
  });
  setResult(res);
};

  const [email, setEmail] = useState("");

  return (
    <div style={{ padding: 24, maxWidth: 700 }}>
      <h2>AI Maturity 360 – Self Assessment</h2>

<input
  type="email"
  placeholder="Work email"
  value={email}
  required
  onChange={e => setEmail(e.target.value)}
  style={{ marginBottom: 20, padding: 8, width: "100%" }}
/>
      {Object.entries(questions).map(([key, question]) => (
        <div key={key} style={{ marginBottom: 16 }}>
          <p>{question}</p>
          <select onChange={e => handleChange(key, Number(e.target.value))}>
            <option value="">Select</option>
            <option value="0">0 – Not present</option>
            <option value="1">1 – Ad-hoc</option>
            <option value="2">2 – Defined</option>
            <option value="3">3 – Optimized</option>
          </select>
        </div>
      ))}

      <button onClick={handleSubmit}>Submit</button>

      {result && (
        <div style={{ marginTop: 24 }}>
          <h3>Maturity Level: {result.maturity_level}</h3>
          <p>Total Score: {result.total_score}</p>
        </div>
      )}
    </div>
  );
}

export default App;
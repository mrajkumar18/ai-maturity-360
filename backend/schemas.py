from pydantic import BaseModel
from typing import Dict, Optional

class AssessmentSubmission(BaseModel):
    email: Optional[str]
    answers: Dict[str, int]  # question_id -> score
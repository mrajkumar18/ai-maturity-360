from database import get_db

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        total_score INTEGER,
        maturity_level TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id INTEGER,
        question_id TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_assessment(email, total_score, maturity_level):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO assessments (email, total_score, maturity_level)
        VALUES (?, ?, ?)
        """,
        (email, total_score, maturity_level)
    )

    conn.commit()
    conn.close()
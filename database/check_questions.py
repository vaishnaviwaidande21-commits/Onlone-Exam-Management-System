
import sqlite3
import os

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "online_exam.db"
)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

rows = cursor.execute("""
    SELECT question_id, question_text
    FROM question
    WHERE question_type = 'True/False'
""").fetchall()

updated = 0

for question_id, question_text in rows:

    if question_text and question_text.strip().endswith("?"):
        new_question = question_text.strip()[:-1] + "."

        cursor.execute("""
            UPDATE question
            SET question_text = ?
            WHERE question_id = ?
        """, (new_question, question_id))

        updated += 1

conn.commit()
conn.close()

print("=" * 50)
print("TRUE/FALSE QUESTION MARK FIXED")
print("=" * 50)
print("Questions updated:", updated)

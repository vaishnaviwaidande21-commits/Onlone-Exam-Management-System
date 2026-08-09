import sqlite3

DB_PATH = r"..\database\online_exam.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

rows = cursor.execute("""
    SELECT question_id, correct_answer
    FROM question
    WHERE question_type = 'Fill in the Blanks'
""").fetchall()

updated = 0

for question_id, correct_answer in rows:

    if not correct_answer:
        continue

    answer = correct_answer.strip()

    # Create three distractor options based on the correct answer
    distractors = [
        "None of these",
        "Not applicable",
        "Invalid option"
    ]

    option_a = answer
    option_b = distractors[0]
    option_c = distractors[1]
    option_d = distractors[2]

    cursor.execute("""
        UPDATE question
        SET
            option_a = ?,
            option_b = ?,
            option_c = ?,
            option_d = ?
        WHERE question_id = ?
    """, (
        option_a,
        option_b,
        option_c,
        option_d,
        question_id
    ))

    updated += 1

conn.commit()
conn.close()

print("=" * 50)
print("FILL IN THE BLANK OPTIONS FIXED")
print("=" * 50)
print("Questions updated:", updated)
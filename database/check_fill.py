import sqlite3

db_path = r"..\database\online_exam.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

rows = cursor.execute("""
    SELECT
        question_id,
        subject,
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer
    FROM question
    WHERE question_type = 'Fill in the Blanks'
    LIMIT 10
""").fetchall()

print("=" * 60)
print("FILL IN THE BLANKS DATA CHECK")
print("=" * 60)

for row in rows:
    print()
    print("ID:", row[0])
    print("Subject:", row[1])
    print("Question:", row[2])
    print("Option A:", row[3])
    print("Option B:", row[4])
    print("Option C:", row[5])
    print("Option D:", row[6])
    print("Correct Answer:", row[7])
    print("-" * 60)

conn.close()
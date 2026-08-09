import sqlite3
import os

DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "online_exam.db"
)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Desired order
subjects = ["Python", "Java", "HTML", "DBMS"]
question_types = [
    "MCQ",
    "True/False",
    "Fill in the Blanks"
]

# Read all existing questions
all_questions = cursor.execute("""
    SELECT
        exam_id,
        topic,
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        subject,
        difficulty,
        question_type
    FROM question
    ORDER BY question_id
""").fetchall()

# Group questions
grouped = {}

for row in all_questions:

    subject = row[8]
    question_type = row[10]

    grouped.setdefault(
        (subject, question_type),
        []
    ).append(row)


# Check each group has 50
for subject in subjects:

    for question_type in question_types:

        count = len(
            grouped.get(
                (subject, question_type),
                []
            )
        )

        print(
            subject,
            "|",
            question_type,
            "|",
            count
        )

        if count != 50:
            raise ValueError(
                f"{subject} - {question_type} "
                f"has {count} questions instead of 50."
            )


# Delete existing questions
cursor.execute("DELETE FROM question")


# Insert in required order
question_id = 1

for subject in subjects:

    for question_type in question_types:

        questions = grouped[
            (subject, question_type)
        ]

        for row in questions:

            cursor.execute("""
                INSERT INTO question
                (
                    question_id,
                    exam_id,
                    topic,
                    question_text,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer,
                    subject,
                    difficulty,
                    question_type
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                question_id,
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10]
            ))

            question_id += 1


conn.commit()


# Verify
total = cursor.execute(
    "SELECT COUNT(*) FROM question"
).fetchone()[0]

print()
print("====================================")
print("QUESTIONS REORDERED SUCCESSFULLY")
print("====================================")
print("Total questions:", total)

print()
print("New order:")

start = 1

for subject in subjects:

    for question_type in question_types:

        end = start + 49

        print(
            f"{start} - {end} : "
            f"{subject} : {question_type}"
        )

        start = end + 1


conn.close()
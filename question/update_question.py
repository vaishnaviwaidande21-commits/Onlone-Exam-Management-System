import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection


def update_question():

    print("\n" + "=" * 50)
    print("          UPDATE QUESTION")
    print("=" * 50)

    question_id = input("Enter Question ID: ")

    question_text = input("Enter New Question: ")

    option_a = input("Enter New Option A: ")
    option_b = input("Enter New Option B: ")
    option_c = input("Enter New Option C: ")
    option_d = input("Enter New Option D: ")

    correct_answer = input("Enter New Correct Answer: ")

    difficulty = input("Enter New Difficulty (Easy/Medium/Hard): ")

    print("\nSelect Question Type")
    print("1. MCQ")
    print("2. True / False")
    print("3. Fill in the Blanks")

    choice = input("Enter Choice: ")

    if choice == "1":
        question_type = "MCQ"

    elif choice == "2":
        question_type = "True/False"

    elif choice == "3":
        question_type = "Fill in the Blanks"

    else:
        print("\nInvalid Question Type!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            UPDATE question
            SET
                question_text = ?,
                option_a = ?,
                option_b = ?,
                option_c = ?,
                option_d = ?,
                correct_answer = ?,
                difficulty = ?,
                question_type = ?
            WHERE question_id = ?
            """,
            (
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                difficulty,
                question_type,
                question_id
            )
        )

        conn.commit()

        if cursor.rowcount > 0:

            print("\n" + "=" * 50)
            print("Question Updated Successfully!")
            print("=" * 50)

        else:

            print("\nQuestion ID Not Found!")

    except Exception as e:

        print("\nError :", e)

    finally:

        conn.close()


if __name__ == "__main__":

    update_question()
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection


def delete_question():

    print("\n===== DELETE QUESTION =====")

    question_id = input("\nEnter Question ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        question_text,
        subject,
        difficulty,
        question_type
        FROM question
        WHERE question_id = ?
        """,
        (question_id,)
    )

    question = cursor.fetchone()

    if not question:

        print("\nQuestion ID Not Found!")
        conn.close()
        return

    print("\n----------------------------------------")
    print("Question :", question[0])
    print("Subject  :", question[1])
    print("Difficulty :", question[2])
    print("Type :", question[3])
    print("----------------------------------------")

    confirm = input("\nAre you sure? (Y/N): ")

    if confirm.lower() != "y":

        print("\nDelete Cancelled.")
        conn.close()
        return

    cursor.execute(
        """
        DELETE FROM question
        WHERE question_id = ?
        """,
        (question_id,)
    )

    conn.commit()

    print("\nQuestion Deleted Successfully!")

    conn.close()


if __name__ == "__main__":
    delete_question()
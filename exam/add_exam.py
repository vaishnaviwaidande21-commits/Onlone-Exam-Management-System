import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_exam():

    print("\n===== Add Exam =====")

    exam_name = input("Enter Exam Name: ")
    subject = input("Enter Subject: ")
    teacher_id = input("Enter Teacher ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO exam(exam_name, subject, teacher_id)
            VALUES(?,?,?)
            """,
            (exam_name, subject, teacher_id)
        )

        conn.commit()

        print("Exam Added Successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    add_exam()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_student():

    print("\n===== Add Student =====")

    name = input("Enter Student Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO student(name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        conn.commit()

        print("\nStudent Added Successfully! ✅")

    except Exception as e:

        print("Error:", e)

    finally:

        conn.close()


if __name__ == "__main__":
    add_student()
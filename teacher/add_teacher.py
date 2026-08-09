import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_teacher():

    print("\n===== Add Teacher =====")

    name = input("Enter Teacher Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    subject = input("Enter Subject: ")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO teacher(name,email,password,subject)
            VALUES(?,?,?,?)
            """,
            (name, email, password, subject)
        )

        conn.commit()
        print("Teacher Added Successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    add_teacher()
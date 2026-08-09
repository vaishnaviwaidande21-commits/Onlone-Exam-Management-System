import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_teacher():

    print("\n===== Update Teacher =====")

    teacher_id = input("Enter Teacher ID: ")

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    password = input("Enter New Password: ")
    subject = input("Enter New Subject: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE teacher
        SET name=?, email=?, password=?, subject=?
        WHERE teacher_id=?
        """,
        (name, email, password, subject, teacher_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Teacher Updated Successfully!")
    else:
        print("Teacher Not Found")

    conn.close()


if __name__ == "__main__":
    update_teacher()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_student():

    print("\n===== Update Student =====")

    student_id = input("Enter Student ID: ")

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    password = input("Enter New Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE student
        SET name=?, email=?, password=?
        WHERE student_id=?
        """,
        (name, email, password, student_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found")

    conn.close()


if __name__ == "__main__":
    update_student()
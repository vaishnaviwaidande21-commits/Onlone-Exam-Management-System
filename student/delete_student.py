import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_student():

    print("\n===== Delete Student =====")

    student_id = input("Enter Student ID to Delete: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM student WHERE student_id=?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found")

    conn.close()


if __name__ == "__main__":
    delete_student()
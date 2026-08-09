import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_teacher():

    print("\n===== Delete Teacher =====")

    teacher_id = input("Enter Teacher ID to Delete: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM teacher WHERE teacher_id=?",
        (teacher_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Teacher Deleted Successfully!")
    else:
        print("Teacher Not Found")

    conn.close()


if __name__ == "__main__":
    delete_teacher()
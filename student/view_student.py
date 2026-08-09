import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def view_students():

    print("\n" + "=" * 70)
    print("                    STUDENT LIST")
    print("=" * 70)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    conn.close()


    if students:

        print("-" * 70)
        print(f"{'ID':<10}{'Student Name':<25}{'Email ID':<35}")
        print("-" * 70)


        for student in students:

            print(
                f"{student[0]:<10}{student[1]:<25}{student[2]:<35}"
            )


        print("-" * 70)
        print("Total Students :", len(students))
        print("=" * 70)


    else:

        print("No Students Found")



if __name__ == "__main__":

    view_students()
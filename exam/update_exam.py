import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def update_exam():

    print("\n" + "=" * 50)
    print("             UPDATE EXAM")
    print("=" * 50)


    exam_id = input("Enter Exam ID: ")


    exam_name = input("Enter New Exam Name: ")

    subject = input("Enter New Subject: ")

    teacher_id = input("Enter New Teacher ID: ")



    conn = get_connection()
    cursor = conn.cursor()



    try:

        cursor.execute(
            """
            UPDATE exam
            SET
            exam_name = ?,
            subject = ?,
            teacher_id = ?

            WHERE exam_id = ?
            """,
            (
                exam_name,
                subject,
                teacher_id,
                exam_id
            )
        )


        conn.commit()


        if cursor.rowcount > 0:

            print("\nExam Updated Successfully!")

        else:

            print("\nExam ID Not Found!")



    except Exception as e:

        print("\nError:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    update_exam()
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def delete_exam():

    print("\n" + "=" * 50)
    print("             DELETE EXAM")
    print("=" * 50)


    exam_id = input("Enter Exam ID to Delete: ")



    conn = get_connection()
    cursor = conn.cursor()



    try:

        cursor.execute(
            """
            DELETE FROM exam
            WHERE exam_id = ?
            """,
            (exam_id,)
        )


        conn.commit()



        if cursor.rowcount > 0:

            print("\nExam Deleted Successfully!")

        else:

            print("\nExam ID Not Found!")



    except Exception as e:

        print("\nError:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    delete_exam()
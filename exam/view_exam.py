import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def view_exam():

    print("\n" + "=" * 70)
    print("                    EXAM LIST")
    print("=" * 70)


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        exam_id,
        exam_name,
        subject,
        teacher_id

        FROM exam
        """
    )


    exams = cursor.fetchall()


    conn.close()



    if not exams:

        print("\nNo Exams Found!")
        return



    for exam in exams:

        print("\n---------------------------------------------")

        print("Exam ID     :", exam[0])
        print("Exam Name   :", exam[1])
        print("Subject     :", exam[2])
        print("Teacher ID  :", exam[3])

        print("---------------------------------------------")



if __name__ == "__main__":

    view_exam()
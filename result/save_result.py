import sys
import os
from datetime import datetime

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def save_result():

    print("\n" + "=" * 50)
    print("             SAVE RESULT")
    print("=" * 50)


    student_id = input("Enter Student ID: ")

    exam_id = input("Enter Exam ID: ")

    score = int(input("Enter Score: "))

    total_questions = int(
        input("Enter Total Questions: ")
    )


    percentage = (score / total_questions) * 100


    exam_date = datetime.now().strftime("%Y-%m-%d")



    conn = get_connection()
    cursor = conn.cursor()



    try:

        cursor.execute(
            """
            INSERT INTO result
            (
            student_id,
            exam_id,
            score,
            total_questions,
            percentage,
            exam_date
            )

            VALUES(?,?,?,?,?,?)

            """,
            (
                student_id,
                exam_id,
                score,
                total_questions,
                percentage,
                exam_date
            )
        )


        conn.commit()


        print("\nResult Saved Successfully!")

        print("Percentage :", round(percentage,2), "%")



    except Exception as e:

        print("\nError:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    save_result()
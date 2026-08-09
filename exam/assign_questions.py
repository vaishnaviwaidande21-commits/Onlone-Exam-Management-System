import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def assign_questions():

    print("\n" + "=" * 60)
    print("             ASSIGN QUESTIONS TO EXAM")
    print("=" * 60)


    exam_id = input("Enter Exam ID: ")


    conn = get_connection()
    cursor = conn.cursor()



    # Get exam subject

    cursor.execute(
        """
        SELECT subject
        FROM exam
        WHERE exam_id = ?
        """,
        (exam_id,)
    )


    exam = cursor.fetchone()



    if not exam:

        print("\nExam Not Found!")
        conn.close()
        return



    subject = exam[0]



    try:


        cursor.execute(
            """
            UPDATE question

            SET exam_id = ?

            WHERE LOWER(subject) = LOWER(?)
            AND exam_id IS NULL

            """,
            (
                exam_id,
                subject
            )
        )



        conn.commit()



        if cursor.rowcount > 0:

            print("\nQuestions Assigned Successfully!")
            print("Subject :", subject)
            print("Total Questions :", cursor.rowcount)


        else:

            print("\nNo Questions Available For This Subject!")



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    assign_questions()
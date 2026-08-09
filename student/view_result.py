import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection


def view_result(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT 
            exam.exam_name,
            exam.subject,
            result.correct_answers,
            result.total_questions,
            result.percentage,
            result.date,
            result.grade,
            result.analysis

        FROM result

        JOIN exam
        ON result.exam_id = exam.exam_id

        WHERE result.student_id = ?

        """, (student_id,))


        results = cursor.fetchall()


        if not results:

            print("\nNo Result Found! ❌")
            return



        print("\n")
        print("="*60)
        print("              STUDENT RESULT")
        print("="*60)



        for result in results:


            print("\nExam Name      :", result[0])

            print("Subject        :", result[1])

            print(
                "Score          :",
                f"{result[2]}/{result[3]}"
            )

            print(
                "Percentage     :",
                f"{result[4]:.2f}%"
            )

            print(
                "Exam Date      :",
                result[5]
            )

            print(
                "Grade          :",
                result[6]
            )


            print("-"*60)


            # AI Performance Analysis

            if result[4] >= 80:

                performance = "Excellent ⭐⭐⭐⭐⭐"


            elif result[4] >= 60:

                performance = "Good ⭐⭐⭐⭐"


            elif result[4] >= 40:

                performance = "Average ⭐⭐⭐"


            else:

                performance = "Need Improvement ⭐⭐"



            print(
                "AI Performance :",
                performance
            )


            if result[7]:

                print(
                    "AI Analysis    :",
                    result[7]
                )


            print("-"*60)



        print("="*60)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":


    student_id = input(
        "Enter Student ID: "
    )


    view_result(student_id)
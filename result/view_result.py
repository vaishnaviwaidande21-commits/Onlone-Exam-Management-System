import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def view_result():

    print("\n" + "=" * 60)
    print("                 VIEW RESULT")
    print("=" * 60)


    student_id = input("Enter Student ID: ")



    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT
        result_id,
        exam_id,
        score,
        total_questions,
        percentage,
        exam_date

        FROM result

        WHERE student_id = ?

        """,
        (student_id,)
    )



    results = cursor.fetchall()



    conn.close()



    if not results:

        print("\nNo Result Found!")

        return



    for result in results:


        print("\n" + "-" * 60)

        print("Result ID       :", result[0])

        print("Exam ID         :", result[1])

        print("Score           :", 
              f"{result[2]}/{result[3]}")

        print("Percentage      :",
              round(result[4],2), "%")

        print("Exam Date       :", result[5])


        print("-" * 60)



if __name__ == "__main__":

    view_result()
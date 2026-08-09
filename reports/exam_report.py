import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def exam_report():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT 
            exam.exam_name,
            exam.subject,
            COUNT(question.question_id)

        FROM exam

        LEFT JOIN question

        ON exam.exam_id = question.exam_id

        GROUP BY exam.exam_id

        """)


        exams = cursor.fetchall()


        if not exams:

            print("\nNo Exam Data Found!")
            return


        print("\n" + "="*65)
        print("                 EXAM REPORT")
        print("="*65)


        print(
            f"{'Exam Name':<25}{'Subject':<15}{'Questions':<10}"
        )


        print("-"*65)


        for exam in exams:

            print(
                f"{exam[0]:<25}{exam[1]:<15}{exam[2]:<10}"
            )


        print("="*65)



    except Exception as e:

        print("Error:", e)


    finally:

        conn.close()



if __name__ == "__main__":

    exam_report()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def student_report():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute("""
        SELECT

        student.name,
        exam.exam_name,
        result.score,
        result.total_questions,
        result.percentage

        FROM result

        JOIN student

        ON result.student_id = student.student_id


        JOIN exam

        ON result.exam_id = exam.exam_id

        """)


        data = cursor.fetchall()


        if not data:

            print("\nNo Student Report Found!")
            return



        print("\n" + "="*70)
        print("                 STUDENT REPORT")
        print("="*70)


        print(
            f"{'Student':<20}{'Exam':<20}{'Score':<10}{'Percentage':<15}"
        )


        print("-"*70)


        for row in data:

            score = f"{row[2]}/{row[3]}"


            print(
                f"{row[0]:<20}{row[1]:<20}{score:<10}{row[4]:.2f}%"
            )


        print("="*70)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    student_report()
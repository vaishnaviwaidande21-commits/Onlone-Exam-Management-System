import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def view_available_exam():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute("""
        SELECT 
            exam_id,
            exam_name,
            subject
        FROM exam
        """)


        exams = cursor.fetchall()



        if not exams:

            print("\nNo Exams Available!")
            return



        print("\n" + "="*60)
        print("             AVAILABLE EXAMS")
        print("="*60)


        print(
            f"{'ID':<5}{'Exam Name':<25}{'Subject':<20}"
        )


        print("-"*60)


        for exam in exams:

            print(
                f"{exam[0]:<5}{exam[1]:<25}{exam[2]:<20}"
            )


        print("="*60)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    view_available_exam()
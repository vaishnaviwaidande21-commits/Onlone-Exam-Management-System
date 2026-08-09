import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from session.user_session import get_user
from student.attempt_question import attempt_question



def start_exam():

    user = get_user()


    if not user or "id" not in user:

        print("\nPlease Login First! ❌")
        return



    student_id = user["id"]


    conn = None


    try:

        print("\n===== Available Exams =====")


        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute("""
            SELECT exam_id, exam_name, subject
            FROM exam
        """)


        exams = cursor.fetchall()



        if not exams:

            print("No Exams Available!")
            return



        print("-" * 60)
        print(f"{'ID':<5}{'Exam Name':<25}{'Subject':<20}")
        print("-" * 60)



        for exam in exams:

            print(
                f"{exam[0]:<5}{exam[1]:<25}{exam[2]:<20}"
            )



        print("-" * 60)



        exam_id = input("\nEnter Exam ID to Start: ")



        # Check Exam Exists

        cursor.execute("""
            SELECT exam_id
            FROM exam
            WHERE exam_id = ?
        """,
        (exam_id,))


        exam = cursor.fetchone()



        if not exam:

            print("\nInvalid Exam ID! ❌")
            return



        print("\nExam Started Successfully! ✅")
        print("Loading Questions...\n")



        # Close database before attempting questions
        conn.close()
        conn = None



        # Start Questions

        attempt_question(
            student_id,
            exam_id
        )



    except Exception as e:

        print("Error:", e)



    finally:

        if conn:

            conn.close()





if __name__ == "__main__":

    start_exam()
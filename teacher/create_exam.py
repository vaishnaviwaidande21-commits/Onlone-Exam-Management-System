import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from session.user_session import get_user



def create_exam():

    user = get_user()


    if not user or "id" not in user:

        print("\nPlease Login First! ❌")
        return



    teacher_id = user["id"]


    conn = get_connection()
    cursor = conn.cursor()


    try:

        print("\n========== CREATE EXAM ==========")


        exam_name = input("Enter Exam Name : ")
        subject = input("Enter Subject   : ")


        cursor.execute("""
        INSERT INTO exam
        (
            exam_name,
            subject,
            teacher_id
        )
        VALUES (?, ?, ?)
        """,
        (
            exam_name,
            subject,
            teacher_id
        ))


        conn.commit()


        print("\nExam Created Successfully! ✅")
        print("Teacher ID :", teacher_id)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    create_exam()
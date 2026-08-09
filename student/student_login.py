import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection
from session.user_session import set_user



def student_login():

    print("\n========================================")
    print("            STUDENT LOGIN")
    print("========================================")


    email = input("Enter Email: ")
    password = input("Enter Password: ")


    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute(
            """
            SELECT
            student_id,
            name,
            email,
            password,
            course

            FROM student

            WHERE email=? AND password=?

            """,
            (email, password)
        )


        student = cursor.fetchone()



        if student:


            set_user(
                student[0],
                student[1],
                "student"
            )


            print("\nStudent Login Successful! ✅")


            # Return logged in student id
            return student[0]



        else:

            print("\nInvalid Email or Password! ❌")

            return None




    except Exception as e:

        print("Student Login Error:", e)

        return None



    finally:

        conn.close()



if __name__ == "__main__":

    student_login()
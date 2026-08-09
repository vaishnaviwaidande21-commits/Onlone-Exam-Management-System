import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from db_connection import get_connection
from session.user_session import set_user
from teacher.teacher_menu import teacher_menu



def teacher_login():

    print("\n" + "=" * 40)
    print("            TEACHER LOGIN")
    print("=" * 40)


    email = input("Enter Email: ")
    password = input("Enter Password: ")



    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT teacher_id, name, email
        FROM teacher
        WHERE email=? AND password=?
        """,
        (email, password)
    )


    teacher = cursor.fetchone()


    conn.close()



    if teacher:


        set_user(
            teacher[0],
            teacher[1],
            "teacher"
        )


        print("\nLogin Successful! ✅")


        teacher_menu()



    else:

        print("\nInvalid Email or Password ❌")



if __name__ == "__main__":

    teacher_login()
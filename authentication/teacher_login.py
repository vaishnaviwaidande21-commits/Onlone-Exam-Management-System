import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from teacher.teacher_menu import teacher_menu
from teacher.register_teacher import register_teacher

from session.user_session import set_user, clear_user



def teacher_login():

    while True:

        print("\n========== TEACHER LOGIN ==========")
        print("1. Login")
        print("2. Register")
        print("3. Back")


        choice = input("Enter your choice: ")



        if choice == "1":


            conn = get_connection()
            cursor = conn.cursor()


            try:

                email = input("Enter Email    : ")
                password = input("Enter Password : ")



                cursor.execute("""
                SELECT teacher_id, name
                FROM teacher
                WHERE email = ? AND password = ?
                """,
                (
                    email,
                    password
                ))



                teacher = cursor.fetchone()



                if teacher:


                    print("\nLogin Successful! ✅")
                    print("Welcome,", teacher[1])



                    # Save Teacher Session

                    set_user(
                        teacher[0],
                        teacher[1],
                        "Teacher"
                    )



                    teacher_menu()



                else:

                    print("\nInvalid Email or Password!")



            except Exception as e:

                print("Error:", e)



            finally:

                conn.close()



        elif choice == "2":


            register_teacher()



        elif choice == "3":


            clear_user()
            break



        else:


            print("Invalid Choice!")




if __name__ == "__main__":

    teacher_login()
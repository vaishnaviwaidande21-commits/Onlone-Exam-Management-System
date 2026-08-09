import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from student.student_menu import student_menu
from student.register_student import register_student
from session.user_session import set_user



def student_login():

    while True:

        print("\n========== STUDENT LOGIN ==========")
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
                SELECT student_id, name
                FROM student
                WHERE email = ? AND password = ?
                """,
                (
                    email,
                    password
                ))


                student = cursor.fetchone()


                if student:

                    print("\nLogin Successful! ✅")
                    print("Welcome,", student[1])


                    # Save Student Session
                    set_user(
                        student[0],
                        student[1],
                        "Student"
                    )


                    student_menu()


                else:

                    print("\nInvalid Email or Password!")


            except Exception as e:

                print("Error:", e)


            finally:

                conn.close()



        elif choice == "2":

            register_student()



        elif choice == "3":

            break



        else:

            print("Invalid Choice!")



if __name__ == "__main__":
    student_login()